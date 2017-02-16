package io.workspace.sse

import java.time.LocalTime
import java.time.format.DateTimeFormatter

import akka.NotUsed
import akka.actor.ActorSystem
import akka.http.scaladsl.Http
import akka.http.scaladsl.model.HttpRequest
import akka.http.scaladsl.server.Directives
import akka.stream.ActorMaterializer
import akka.http.scaladsl.unmarshalling.Unmarshal
import akka.stream.scaladsl.Source
import de.heikoseeberger.akkasse.{EventStreamMarshalling, EventStreamUnmarshalling, ServerSentEvent}

import scala.concurrent.duration._
import scala.io.StdIn

object Main {

  implicit val system = ActorSystem("my-system")
  implicit val materializer = ActorMaterializer()
  // needed for the future flatMap/onComplete in the end
  implicit val executionContext = system.dispatcher

  def main(args: Array[String]): Unit = {

    val host = "localhost"
    val port = 8085

    println("starting server")
    val bindingFuture = startServer(host, port)

    Thread.sleep(3000)
    println("starting client")
    startClient(host, port)

    StdIn.readLine() // let it run until user presses return
    bindingFuture
      .flatMap(_.unbind()) // trigger unbinding from the port
      .onComplete(_ => system.terminate()) // and shutdown when done

  }

  private def startClient(hostIp: String, port: Int) = {
    import EventStreamUnmarshalling._ // That does the trick!

    Http()
      .singleRequest(HttpRequest(uri = s"http://$hostIp:$port/events"))
      .flatMap(Unmarshal(_).to[Source[ServerSentEvent, NotUsed]])
      .foreach(_.runForeach(print))
  }

  private def startServer(hostIp: String, port: Int) = {

    import Directives._
    import EventStreamMarshalling._ // That does the trick!

    val route =
      path("events") {
        get {
          complete {
            Source
              .tick(2.seconds, 2.seconds, NotUsed)
              .map(_ => LocalTime.now())
              .map(timeToServerSentEvent)
              .keepAlive(1.second, () => ServerSentEvent.heartbeat)
          }
        }
      } ~ path("test"){
        get{
          pathEndOrSingleSlash{
            complete("ok")
          }
        }
      }

    val bindingFuture = Http().bindAndHandle(route, hostIp, port)
    println(s"Server online at http://$hostIp:$port/")

    bindingFuture
  }

  private def timeToServerSentEvent(time: LocalTime) =
    ServerSentEvent(DateTimeFormatter.ISO_LOCAL_TIME.format(time))
}
