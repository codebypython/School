cmake_minimum_required(VERSION 3.25)

# ── Test executables ──────────────────────────────────────────────────────────
add_executable(test_dynamic_array test_dynamic_array.cpp)
target_link_libraries(test_dynamic_array
    PRIVATE
        algocore
        Catch2::Catch2WithMain
)

# Register with CTest via Catch2's discover helper
catch_discover_tests(test_dynamic_array)

# Future test suites — uncomment as headers are implemented:
# add_executable(test_linked_list test_linked_list.cpp)
# target_link_libraries(test_linked_list PRIVATE algocore Catch2::Catch2WithMain)
# catch_discover_tests(test_linked_list)
