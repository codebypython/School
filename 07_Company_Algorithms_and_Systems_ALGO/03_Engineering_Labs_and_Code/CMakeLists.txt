cmake_minimum_required(VERSION 3.25)

project(
    AlgoCoreLabs
    VERSION 1.0.0
    DESCRIPTION "AlgoCore Systems Corp — C++20 Labs & Data Structures (CORP-07-ALGO)"
    LANGUAGES CXX
)

# ── Language standard ──────────────────────────────────────────────────────
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)   # enforce -std=c++20, not -std=gnu++20

# ── Modules ────────────────────────────────────────────────────────────────
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
include(Warnings)
include(Sanitizers)

# ── Fetch Catch2 v3 for TDD ────────────────────────────────────────────────
include(FetchContent)
FetchContent_Declare(
    Catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG        v3.5.2
    GIT_SHALLOW    TRUE
)
FetchContent_MakeAvailable(Catch2)
list(APPEND CMAKE_MODULE_PATH "${catch2_SOURCE_DIR}/extras")
include(CTest)
include(Catch)

# ── Header-only library: algocore ──────────────────────────────────────────
add_library(algocore INTERFACE)
target_include_directories(algocore INTERFACE
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)
target_link_libraries(algocore INTERFACE algocore_warnings)
target_compile_features(algocore INTERFACE cxx_std_20)

# Enable sanitizers on algocore (propagates to all consumers)
enable_sanitizers(algocore)

# ── Subdirectories ─────────────────────────────────────────────────────────
add_subdirectory(labs)
add_subdirectory(tests)

# ── Summary ────────────────────────────────────────────────────────────────
message(STATUS "")
message(STATUS "╔══════════════════════════════════════════════╗")
message(STATUS "║  AlgoCore Systems — C++20 Lab Environment    ║")
message(STATUS "╠══════════════════════════════════════════════╣")
message(STATUS "║  Compiler   : ${CMAKE_CXX_COMPILER_ID} ${CMAKE_CXX_COMPILER_VERSION}")
message(STATUS "║  Standard   : C++${CMAKE_CXX_STANDARD}")
message(STATUS "║  ASAN       : ${ENABLE_ASAN}")
message(STATUS "║  TSAN       : ${ENABLE_TSAN}")
message(STATUS "║  Build type : ${CMAKE_BUILD_TYPE}")
message(STATUS "╚══════════════════════════════════════════════╝")
message(STATUS "")
