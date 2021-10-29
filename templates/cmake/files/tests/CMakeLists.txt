find_package(GTest)
if(GTEST_FOUND)
  include(GoogleTest)

  set(HEADERS
    ${PROJECT_SOURCE_DIR}/include
    ${PROJECT_SOURCE_DIR}/third_party)

  file(GLOB SOURCES
    # Library
		# <put your source files here...>

    # Unit Tests
    main.cpp)

  add_executable(unittest ${SOURCES})
  target_include_directories(unittest PRIVATE ${HEADERS})
  target_link_libraries(unittest gtest)
  target_link_libraries(unittest fmt)

  gtest_add_tests(TARGET unittest)
endif()
