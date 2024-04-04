cmake_minimum_required(VERSION 3.5)
project(plasys_house_world)

find_package(ament_cmake QUIET)

if(ament_cmake_FOUND)
  message(STATUS "Ament found." )
else()
  message(FATAL_ERROR "Ament was not found. Unable to build." )
endif()

find_package(gazebo_ros REQUIRED)

install(DIRECTORY launch worlds models DESTINATION share/${PROJECT_NAME})

ament_export_dependencies(gazebo_ros)
ament_package()
