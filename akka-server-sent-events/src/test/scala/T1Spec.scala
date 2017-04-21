import org.scalatest._

class Notification(receiver: String) {

  private var isRead: Boolean = false
  def getIsRead = isRead

  /*
    return true if isReady not null, otherwise return false (case receiver cannot be empty empty if its null)
   */
  def validReceiver() = receiver != null

  /*
    isTrue != true (false) || isTrue != false (true) -> isTrue always true
   */
  def markAsRead() = isRead = true

  def status() = isRead match {
    case true => "read"
    case false => "unread"
  }
}

class NotificationSpec extends FlatSpec with Matchers {

  "validReceiver" should "true if receiver is not null" in {
    val target = new Notification("something")
    assert(target.validReceiver())
  }

  "validReceiver" should "true if receiver is not empty" in {
    val target = new Notification("something")
    assert(target.validReceiver())
  }

  "validReceiver" should "false if receiver is null" in {
    val target = new Notification(null)
    assert(!target.validReceiver())
  }

  "markAsRead" should "read/unread test" in {
    val target = new Notification("something")
    assert(!target.getIsRead)
    target.markAsRead()
    assert(target.getIsRead)
  }

  "status" should "read/unread" in {
    val target = new Notification("something")
    assert(target.status() == "unread")
    target.markAsRead()
    assert(target.status() == "read")
  }

}

class EmailNotification(receiver: String) extends Notification(receiver: String){
  override def status(): String = s"${super.status()}-email"
}

class EmailNotificationSpec extends FlatSpec with Matchers {

  val statusPostfix = "-email"

  "status" should "read/unread with email" in {
    val target = new EmailNotification("something")
    assert(target.status() == s"unread$statusPostfix")
    target.markAsRead()
    assert(target.status() == s"read$statusPostfix")
  }
}