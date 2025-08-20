  cmake_minimum_required(VERSION 3.8)
  project(my_cpp_pkg)

  if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
  endif()

  # Find dependencies
  find_package(ament_cmake REQUIRED)
  find_package(rclcpp REQUIRED)
  find_package(example_interfaces REQUIRED)
  find_package(sensor_msgs REQUIRED)

  # KTN: For each new executable, add another add_executable() and ament_target_dependencies()

  # KTN: Adds a new executable with the add_executable() function
  # KTN: We also choose the name for the executable, which is test_node
  add_executable(test_node src/first_node.cpp)
  add_executable(number_publisher src/number_publisher.cpp)
  add_executable(number_counter src/number_counter.cpp)

  # KTN: Links all dependencies for the executable with the ament_target_dependencies() function
  ament_target_dependencies(test_node rclcpp)
  ament_target_dependencies(number_publisher rclcpp example_interfaces)
  ament_target_dependencies(number_counter rclcpp example_interfaces)

  # KTN: Install the executable with the install() instruction
  install(TARGETS
    test_node
    number_publisher
    number_counter
    DESTINATION lib/${PROJECT_NAME}
  )

  # If statement is used for build testing
  # If you are NOT doing build testing, you can comment out this block
  # if(BUILD_TESTING)
  #   find_package(ament_lint_auto REQUIRED)

  #   # The following line skips the linter which checks for copyrights
  #   # Comment the line when a copyright and license is added to all source files
  #   set(ament_cmake_copyright_FOUND TRUE)

  #   # The following line skips cpplint (only works in a git repo)
  #   # Comment the line when this package is in a git repo and when
  #   # a copyright and license is added to all source files
  #   set(ament_cmake_cpplint_FOUND TRUE)

  #   ament_lint_auto_find_test_dependencies()
  # endif()

  ament_package()
