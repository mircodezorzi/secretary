find_package(benchmark)
if(benchmark_FOUND)
  file(GLOB SOURCES
    ${PROJECT_SOURCE_DIR}/benchmarks/main.cpp)

  add_executable(bench ${SOURCES})

	target_link_libraries(bench
		PUBLIC
		pthread
		CONAN_PKG::fmt
		CONAN_PKG::benchmark)
endif()
