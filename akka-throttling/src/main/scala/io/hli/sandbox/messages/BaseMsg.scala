package io.hli.sandbox.messages

abstract class BaseMsg extends java.io.Serializable

case class Msg1(name: String) extends BaseMsg
case class Msg2(name: String, id: Int) extends BaseMsg