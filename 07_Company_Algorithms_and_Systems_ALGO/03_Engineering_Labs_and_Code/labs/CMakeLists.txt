cmake_minimum_required(VERSION 3.25)

# ── Labs subdirectory ─────────────────────────────────────────────────────────
# Each week's lab is an independent executable

add_executable(lab1_memory_layout
    Week01_Memory_And_Pointers/lab1_memory_layout.cpp
)
target_link_libraries(lab1_memory_layout PRIVATE algocore)

# Future labs — uncomment as they are created:
# add_executable(lab2_raii       Week02_Smart_Pointers_RAII/lab2_raii.cpp)
# target_link_libraries(lab2_raii PRIVATE algocore)
