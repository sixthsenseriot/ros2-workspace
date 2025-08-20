#include "rclcpp/rclcpp.hpp" // Include the C++ library for ROS2 - Contains the rclcpp::Node class

// Create a class that inherits from the ROS2 Node class
class MyCustomNode : public rclcpp::Node 
{
    public: 
        MyCustomNode() : Node("first_test_node_cpp"), counter_(0) {
            // timer_ follows a common OOP naming convention to specify that a variable is a
            // class attribute
            // Here we create a timer variable so that we can callback a function every 1.0 seconds
            // The callback function will print `Hello ` followed by a counter each time
            timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                             std::bind(&MyCustomNode::print_hello, this));
        }
        void print_hello() {
            RCLCPP_INFO(this->get_logger(), "Hello %d", counter_);
            counter_++;
        }

    private:
        int counter_;

        // Create a shared pointer
        rclcpp::TimerBase::SharedPtr timer_;
};

// Main function to be able to run C++ program
int main(int argc, char **argv)
{
    // Line to initialize ROS2 communications
    rclcpp::init(argc, argv);

    // Create a node object from newly written class
    auto node = std::make_shared<MyCustomNode>();

    // Spin node to continuously run program
    rclcpp::spin(node);

    // Shutdown all ROS2 communication after Ctrl + C is pressed
    rclcpp::shutdown();

    // Return 0 to indicate successful execution of program
    return 0;
}