# Sanitizers.cmake — AddressSanitizer + UBSan configuration
# Usage: include(cmake/Sanitizers.cmake) then call enable_sanitizers(target)

option(ENABLE_ASAN  "Enable AddressSanitizer + UndefinedBehaviorSanitizer" OFF)
option(ENABLE_TSAN  "Enable ThreadSanitizer (mutually exclusive with ASAN)" OFF)

function(enable_sanitizers target)
    if(MSVC)
        # MSVC supports /fsanitize=address from VS2019 16.9+
        if(ENABLE_ASAN)
            target_compile_options(${target} PRIVATE /fsanitize=address)
            message(STATUS "[Sanitizer] ASAN enabled for ${target} (MSVC mode)")
        endif()
        return()
    endif()

    if(ENABLE_ASAN AND ENABLE_TSAN)
        message(FATAL_ERROR "ASAN and TSAN cannot be enabled simultaneously.")
    endif()

    if(ENABLE_ASAN)
        target_compile_options(${target} PRIVATE
            -fsanitize=address,undefined
            -fno-omit-frame-pointer
            -g
        )
        target_link_options(${target} PRIVATE
            -fsanitize=address,undefined
        )
        message(STATUS "[Sanitizer] ASan + UBSan enabled for ${target}")
    endif()

    if(ENABLE_TSAN)
        target_compile_options(${target} PRIVATE
            -fsanitize=thread
            -fno-omit-frame-pointer
            -g
        )
        target_link_options(${target} PRIVATE
            -fsanitize=thread
        )
        message(STATUS "[Sanitizer] TSan enabled for ${target}")
    endif()
endfunction()
