#!/usr/bin/env python3
import rclpy # Python library for ROS 2
from rclpy.node import Node # Getting the Node class from the library

# New class that inherits the rclpy Node class (able to access all ROS2 functionalities)
class MyCustomNode(Node) :
    def __init__(self) :
        
        # .super() provides a way to access methods / props of a parent or sibling class
        # In this case, .super() is calling the parent constructor
        # (This is also where you will specify the node name)
        super().__init__('first_test_node_py') 

        # Prints "Hello World" when the node starts
        # .get_logger() is the logging functionality
        # .info() is to print a log with the info level
        self.get_logger().info("Hello World") 

def main(args=None) :
    # Line to initialize ROS2 communications
    # Should be first line in main
    rclpy.init(args=args)

    # Create an object from the MyCustomNode class (this is our node)
    # Initializes the node (no need to destroy later because handles that on exit)
    node = MyCustomNode()

    # Makes the node spin (pressing Ctrl + C will stop this process)
    # .spin() will block the execution here & the program stays alive along with the node
    # Without this line, the program will exit here and the node will be destroyed
    rclpy.spin(node)

    # When Ctrl + C is pressed (AKA the node is killed), the line below will
    # shutdown ROS2 communications
    # Should be last line in main 
    rclpy.shutdown()

# Line to call main() function if you run the Python script directly
if __name__ == '__main__':
    main()