import akka.actor.ActorSystem
import akka.testkit.{ImplicitSender, TestKit}
import org.scalatest._

class TemplateSpec
  extends TestKit(ActorSystem("test1"))
  with ImplicitSender
  with WordSpecLike
  with Matchers {

  "story" must {

    "case 1" in {

      assert(true)
    }
  }
}
