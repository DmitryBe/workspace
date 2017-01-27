package io.sandbox

import akka.actor.ActorSystem
import kamon.Kamon
import org.slf4j.LoggerFactory

object Main {

  val logger = LoggerFactory.getLogger("Hello")
  def main(args: Array[String]): Unit = {
    println("start")
    Kamon.start()
    logger.debug("start actor system")
    val system = ActorSystem("SjmClusterSystem")
    val actor = system.actorOf(LogActor.props, "actor1")
    1 to 100 foreach { i =>
      actor ! LogActor.Command1(s"msg-$i")
      println(s"send-$i")
      Thread.sleep(500)
    }
    logger.info("stop actor system")
//    logger.error("this is error2", new Exception("test exception"))
  }
}
