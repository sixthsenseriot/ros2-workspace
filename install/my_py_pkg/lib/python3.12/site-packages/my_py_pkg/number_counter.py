#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter") 
        
        self.counter_ = 0

        # Uses create_subscription() method from the Node class
        # We provide 4 arguments in this method:
        #   1. Topic interface - Needs to be the same for both the publisher & subscriber
        #   2. Topic name - Set to "number"
        #   3. Callback function - Used to process the message from the topic
        #   4. Queue size - Preferred to set to 10
        self.number_subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        
        self.get_logger().info("Number Counter has been started...")

    # Our callback member function
    # Recommended to name callback methods for topics `callback_<topic>`
    # Here we receive the message directly in the parameters of the function (i.e. msg: Int64)
    def callback_number(self, msg: Int64):
        self.counter_ += msg.data
        self.get_logger().info("Counter: " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()