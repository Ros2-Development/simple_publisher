import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")   # Node name 

        self.pub_ = self.create_publisher(String, "Hello", 10)  # Publisher

        self.counter_ = 0
        self.frequency_ = 1.0  # Use a float value for the timer interval in seconds

        self.get_logger().info("Publishing at %d Hz" % self.frequency_)

        # Timer that triggers the callback at the specified frequency
        self.timer_ = self.create_timer(self.frequency_, self.timerCallback)

    def timerCallback(self):
        msg = String()
        msg.data = "Hello ROS2 - counter: %d" % self.counter_

        self.pub_.publish(msg)
        self.counter_ += 1


def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()  # Correct method for shutting down ROS2


if __name__ == '__main__':
    main()
