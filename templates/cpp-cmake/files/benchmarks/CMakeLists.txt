find_package(benchmark)
if(benchmark_FOUND)
  file(GLOB SOURCES
    ${PROJECT_SOURCE_DIR}/benchmarks/main.cpp)

  add_executable(bench ${SOURCES})

  target_link_libraries(bench benchmark)
  target_link_libraries(bench fmt)
  target_link_libraries(bench pthread)
endif()
