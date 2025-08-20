#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberPublisherNode(Node): 
    # Constructor of this class (a special member function)
    def __init__(self):
        super().__init__("number_publisher") 

        # Set a class member variable to send the same number every time to publish to the topic
        self.number_ = 2

        # To create a publisher, we'll use the create_publisher() method from the Node class
        # We use three arguments in this method: 
        #   1. Topic interface: Int64 from the example_interfaces package
        #   2. Topic name: Defined as "number"
        #   3. Queue size: Messages are buffered (up to 10) if messages are published too fast
        self.number_publisher_ = self.create_publisher(Int64, "number", 10)

        # We create a timer using the create_timer method from the Node class here
        # Here we want the publish_number() method to be called every 0.1 second
        self.number_timer_ = self.create_timer(1.0, self.publish_number)
        
        # Print to the shell / console when the node starts
        self.get_logger().info("Number publisher has been started...")

    # Method of this class - This is our callback function
    def publish_number(self):

        # Line below creates an object from the Int64 class
        # This is the interface (the message to send)
        msg = Int64()

        # Here, we provide a number in the data field of the message
        msg.data = self.number_

        # Publishes the message using the publish() method from the number_publisher_ variable
        self.number_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()