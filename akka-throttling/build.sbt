name := """akka-throttling"""

version := "1.0"

scalaVersion := "2.11.8"

// Change this to another test framework if you prefer
libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor" % "2.4.17",
  "joda-time" % "joda-time" % "2.9.9",
  "com.typesafe.akka" %% "akka-contrib" % "2.4.17",

  "com.github.romix.akka" % "akka-kryo-serialization_2.11" % "0.5.0",

  "com.typesafe.akka" %% "akka-testkit" % "2.4.17" % "test",
  "org.scalatest" %% "scalatest" % "2.2.4" % "test"
)

