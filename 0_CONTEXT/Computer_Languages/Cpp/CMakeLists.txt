cmake_minimum_required(VERSION 3.16)
project(ActiveInferenceCpp VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Find optional Eigen library
find_package(Eigen3 QUIET)
if(Eigen3_FOUND)
    message(STATUS "Found Eigen3 - enabling advanced features")
    set(USE_EIGEN ON)
else()
    message(STATUS "Eigen3 not found - using basic implementation")
    set(USE_EIGEN OFF)
endif()

# Create executable
add_executable(ActiveInferenceDemo
    src/main.cpp
    src/ActiveInferenceAgent.cpp
)

# Include directories
target_include_directories(ActiveInferenceDemo PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# Link libraries if Eigen is available
if(USE_EIGEN)
    target_link_libraries(ActiveInferenceDemo PRIVATE Eigen3::Eigen)
    target_compile_definitions(ActiveInferenceDemo PRIVATE USE_EIGEN)
endif()

# Compiler warnings and optimization
target_compile_options(ActiveInferenceDemo PRIVATE
    -Wall
    -Wextra
    -Wpedantic
    -O3
)
