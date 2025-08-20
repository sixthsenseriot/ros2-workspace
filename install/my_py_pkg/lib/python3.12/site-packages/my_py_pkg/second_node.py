#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 

class MyCustomNode(Node) :
    def __init__(self) :
        super().__init__('second_test_node_py') 
        
        # Trailing underscore _ at the end of each class attribute is a common OOP convention to 
        # specify that a variable is a class attribute
        self.counter_ = 0

        # The line below will call the `print_hello` method every 1.0 second
        # .create_timer() method is derived from the Node class - Used to register a callback
        # The method takes in two arguments:
        #   1. The rate that we want to call the function (a float number)
        #   2. The callback function
        self.timer_ = self.create_timer(1.0, self.print_hello)

    def print_hello(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1

def main(args=None) :

    rclpy.init(args=args)
    node = MyCustomNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()