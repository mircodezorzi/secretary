file(GLOB SOURCES
  ${PROJECT_SOURCE_DIR}/src/main.cpp)

set(HEADERS
  ${PROJECT_SOURCE_DIR}/include
  ${PROJECT_SOURCE_DIR}/third_party)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCES})
target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE ${HEADERS})
target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -Wall -Wextra -Wpedantic)

target_link_libraries(${CMAKE_PROJECT_NAME} fmt)
