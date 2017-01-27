import _root_.sbt.Keys._
import com.typesafe.sbt.SbtAspectj._

name := """slf4j"""

version := "1.0"

scalaVersion := "2.11.7"

resolvers += "Sonatype Nexus Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots"

val kamonVersion = "0.6.1"

// Change this to another test framework if you prefer
libraryDependencies ++= Seq(
  "org.slf4j" % "slf4j-api" % "1.7.21",
  "ch.qos.logback" % "logback-classic" % "1.1.3",
  "ch.qos.logback" % "logback-core" % "1.1.3",
  "com.internetitem" % "logback-elasticsearch-appender" % "1.3",
  "com.typesafe.akka" %% "akka-actor" % "2.4.8",
  "org.scalatest" %% "scalatest" % "2.2.4" % "test",

  "io.kamon" %% "kamon-core" % kamonVersion,
  "io.kamon" %% "kamon-akka" % kamonVersion,
  "io.kamon" %% "kamon-akka-remote" % kamonVersion,
  "io.kamon" %% "kamon-statsd" % kamonVersion,
  "io.kamon" %% "kamon-log-reporter" % kamonVersion,
  "io.kamon" %% "kamon-system-metrics" % kamonVersion,

  "org.aspectj" % "aspectjweaver" % "1.8.9"
)

aspectjSettings

javaOptions <++= AspectjKeys.weaverOptions in Aspectj

packAutoSettings

// when you call "sbt run" aspectj weaving kicks in
fork in run := true
