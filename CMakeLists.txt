cmake_minimum_required(VERSION 3.5)
project(plasys_house_world)

find_package(ament_cmake QUIET)

if(ament_cmake_FOUND)
  message(STATUS "Ament found." )
else()
  message(FATAL_ERROR "Ament was not found. Unable to build." )
endif()

find_package(ros_gz_sim REQUIRED)

install(DIRECTORY launch worlds models DESTINATION share/${PROJECT_NAME})

ament_export_dependencies(ros_gz_sim)
ament_package()
