cmake_minimum_required(VERSION 3.10)

project(
    "CV_Project"
    LANGUAGES C CXX
    )

set(CMAKE_CXX_STANDARD 17)
message(STATUS "-std=C++17")

# == Third Party ==

# OpenCV
find_package(OpenCV PATHS ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/opencv/build)
if (${OpenCV_FOUND})
    message(STATUS "OpenCV Found...")

    include_directories(
        ${OpenCV_INCLUDE_DIRS}
    )
else (${OpenCV_FOUND})
    message(STATUS "OpenCV NOT Found...")
endif (${OpenCV_FOUND})


include_directories(
    include/
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

add_executable(project
    src/main.cpp
)

target_link_libraries(project
    ${OpenCV_LIBS}
)