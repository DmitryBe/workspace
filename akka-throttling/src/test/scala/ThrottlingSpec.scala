import java.util.concurrent.TimeUnit

import akka.actor.Actor.Receive
import akka.actor.{Actor, ActorSystem, Props}
import akka.contrib.throttle.Throttler.{Rate, SetTarget}
import akka.contrib.throttle.TimerBasedThrottler
import akka.testkit.{ImplicitSender, TestKit}
import org.scalatest._
import org.joda.time._
import scala.concurrent.duration.Duration

class ThrottlingSpec
  extends TestKit(ActorSystem("test1"))
  with ImplicitSender
  with WordSpecLike
  with Matchers {

  "story" must {

    "case 1" in {

      val printerA = system.actorOf(Props(new Actor{
        override def receive: Receive = {
          case msg =>
            val time = DateTime.now()
            println(s"[$time]: $msg")
        }
      }))

      // throttle actor
      val throttlerPrinterA = system.actorOf(Props(
        new TimerBasedThrottler(Rate(3, Duration(1, TimeUnit.SECONDS)))
      ))
      throttlerPrinterA ! SetTarget(Some(printerA))

      1 to 10 foreach{ i =>
        throttlerPrinterA ! s"msg-$i"
      }

      Thread.sleep(5000)
      assert(true)
    }
  }
}
