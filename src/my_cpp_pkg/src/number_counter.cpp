#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

using namespace std::placeholders;

class NumberCounterNode : public rclcpp::Node
{
public:
    NumberCounterNode() : Node("number_counter")
    {   
        // Create a class member variable with create_subscription method
        // Takes in 3 arguments:
        //  1. Topic interface
        //  2. Topic name
        //  3. Queue size
        number_subscriber_ = this->create_subscription<example_interfaces::msg::Int64>(
            "number",
            10,
            std::bind(&NumberCounterNode::callbackNumber, this, _1)
        );

        RCLCPP_INFO(this->get_logger(), "Number counter has been started...");
    }

    void callbackNumber(const example_interfaces::msg::Int64::SharedPtr msg) {
        counter_ += msg->data;
        RCLCPP_INFO(this->get_logger(), "Counter: %d", counter_);
    }

private:

    int counter_ = 0;
    
    // Declare the subscriber object as a private attribute
    rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr number_subscriber_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberCounterNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}