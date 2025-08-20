#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

class NumberPublisherNode : public rclcpp::Node
{
public:
    NumberPublisherNode() : Node("number_publisher")
    {
        // Use the create_publisher() method from the Node class
        number_publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10);

        number_timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                                std::bind(&NumberPublisherNode::publishNumber, this));
        RCLCPP_INFO(this->get_logger(), "Number publisher has been started...");
    }
    void publishNumber() {
        auto msg = example_interfaces::msg::Int64();
        msg.data = number_;
        number_publisher_->publish(msg);
    }

private:

    // Declare our publisher as a private member variable in the class
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr number_publisher_;

    rclcpp::TimerBase::SharedPtr number_timer_;

    std::int64_t number_ = 2;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}