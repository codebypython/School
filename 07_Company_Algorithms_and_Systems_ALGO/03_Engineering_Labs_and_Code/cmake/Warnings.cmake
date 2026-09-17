# Warnings.cmake — Strict compiler warnings for AlgoCore C++20 labs
# Usage: include(cmake/Warnings.cmake) then target_link_libraries(target PRIVATE algocore_warnings)

add_library(algocore_warnings INTERFACE)

if(MSVC)
    target_compile_options(algocore_warnings INTERFACE
        /W4
        /WX           # warnings as errors
        /wd4996       # allow POSIX names
        /permissive-  # strict standards conformance
        /Zc:__cplusplus
    )
else()
    # GCC / Clang
    target_compile_options(algocore_warnings INTERFACE
        -Wall
        -Wextra
        -Wpedantic
        -Werror               # warnings as errors
        -Wconversion
        -Wsign-conversion
        -Wshadow
        -Wnon-virtual-dtor
        -Wold-style-cast
        -Wcast-align
        -Wunused
        -Woverloaded-virtual
        -Wnull-dereference
        -Wdouble-promotion
        -Wformat=2
        -Wmisleading-indentation
    )
endif()
