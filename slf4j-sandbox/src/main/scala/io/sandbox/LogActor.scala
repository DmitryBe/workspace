package io.sandbox

import akka.actor.{Actor, ActorLogging, Props}
import io.sandbox.LogActor.Command1
import kamon.Kamon
import kamon.trace.Tracer
import kamon.util.{Latency, SameThreadExecutionContext}
import org.slf4j.LoggerFactory

import scala.concurrent.Future

object LogActor {
  def props = Props(classOf[LogActor])

  case class Command1(m: String)
}

trait TLogger {
  val logger = LoggerFactory.getLogger(this.getClass)
}

trait KamonSupport {
  def counter(name: String) = Kamon.metrics.counter(name)
  def minMaxCounter(name: String) = Kamon.metrics.minMaxCounter(name)
  def time[A](name: String)(thunk: => A) = Latency.measure(Kamon.metrics.histogram(name))(thunk)
  def traceFuture[A](name:String)(future: => Future[A]):Future[A] =
    Tracer.withContext(Kamon.tracer.newContext(name)) {
      future.andThen { case completed ⇒ Tracer.currentContext.finish() }(SameThreadExecutionContext)
    }
}

class LogActor extends Actor with TLogger with KamonSupport{

  @scala.throws[Exception](classOf[Exception])
  override def preStart(): Unit = {
    logger.info("actor start")
  }

  @scala.throws[Exception](classOf[Exception])
  override def postStop(): Unit = {
    logger.warn(s"actor stop")
  }

  def receive = {
    case msg: Command1 =>
      minMaxCounter("minMaxCounter").increment()
      counter("counter").increment()
      logger.info(s"receive message: ${msg.m}")
  }
}
