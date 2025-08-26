cmake_minimum_required(VERSION 3.16)
project(ActiveInferenceCpp VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Find required packages
find_package(Eigen3 REQUIRED)
find_package(Threads REQUIRED)

# Create executable
add_executable(active_inference_demo
    src/main.cpp
    src/ActiveInferenceAgent.cpp
    src/AntColonyEnvironment.cpp
    src/MatrixUtils.cpp
)

# Include directories
target_include_directories(active_inference_demo PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${EIGEN3_INCLUDE_DIR}
)

# Link libraries
target_link_libraries(active_inference_demo PRIVATE
    Eigen3::Eigen
    Threads::Threads
)

# Compiler warnings
target_compile_options(active_inference_demo PRIVATE
    -Wall
    -Wextra
    -Wpedantic
    -Wshadow
    -Wconversion
    -O3
)

# Enable testing
enable_testing()
add_subdirectory(tests)
