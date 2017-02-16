name := """akka-server-sent-events"""

version := "1.0"

scalaVersion := "2.11.7"

resolvers += Resolver.bintrayRepo("hseeberger", "maven")

libraryDependencies ++= Vector(
  "de.heikoseeberger" %% "akka-sse" % "2.0.0",

  "com.typesafe.akka" %% "akka-actor" % "2.4.17",
  "com.typesafe.akka" %% "akka-contrib" % "2.4.17",
  "com.typesafe.akka" %% "akka-stream" % "2.4.17",
  "com.typesafe.akka" %% "akka-stream-testkit" % "2.4.17",

  "org.scalatest" %% "scalatest" % "2.2.4" % "test"
)
