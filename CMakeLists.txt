cmake_minimum_required(VERSION 3.9)
project(pytdlib)

set(CMAKE_CXX_STANDARD 14)
set(SOURCES
        src/wrapper.cpp
        src/wrappers/td/td_api_wrapper.cpp
        src/wrappers/tl/TlObject_wrapper.cpp
        src/wrappers/telegram/Client_wrapper.cpp
        src/wrappers/telegram/ClientActor_wrapper.cpp)

include_directories(
        ./td/td
        ./td/tddb
        ./td/tdactor
        ./td/tdnet
        ./td/tdtl
        ./td/tdutils
        $ENV{BOOST_PATH}
        $ENV{PYTHON_INCLUDE_PATH}
)

add_library(pytdlib SHARED ${SOURCES})