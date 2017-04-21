import akka.actor.ActorSystem
import akka.testkit.{ImplicitSender, TestKit}
import org.scalatest._
import akka.serialization._
import com.romix.akka.serialization.kryo.KryoSerializer
import io.hli.sandbox.messages.{BaseMsg, Msg1, Msg2}

class SerializerSpec
  extends TestKit(ActorSystem("test1"))
  with ImplicitSender
  with WordSpecLike
  with Matchers {

  "story" must {

    "case 1" in {

      val serialization = SerializationExtension(system)
      val msg = Msg1("test")

      val serializer = serialization.findSerializerFor(msg)
      serializer.isInstanceOf[KryoSerializer] should be(true)

      val serializer2 = serialization.findSerializerFor(Msg2("test2", 11))
      serializer2.isInstanceOf[KryoSerializer] should be(true)

      val serializer3 = serialization.findSerializerFor("test msg str")
      serializer3.isInstanceOf[JavaSerializer] should be(true)

      val bytes = serializer.toBinary(msg)

      val back = serializer.fromBinary(bytes)
      back should be(msg)

      assert(true)
    }
  }
}
