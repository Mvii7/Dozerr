# SPDX-FileCopyrightText: Copyright 2026 Lichii Emulator Project
# SPDX-License-Identifier: GPL-3.0-or-later

add_executable(dozerr-updater main.cpp ../frontend_common/update_installer.cpp)
target_include_directories(dozerr-updater PRIVATE ${PROJECT_SOURCE_DIR}/src)
target_compile_features(dozerr-updater PRIVATE cxx_std_20)
target_link_libraries(dozerr-updater PRIVATE user32 shell32)
set_target_properties(dozerr-updater PROPERTIES WIN32_EXECUTABLE ON)

# The helper runs from a temporary folder, away from the DLLs next to dozerr.exe.
if (MSVC)
    set_property(TARGET dozerr-updater PROPERTY MSVC_RUNTIME_LIBRARY
                 "MultiThreaded$<$<CONFIG:Debug>:Debug>")
else()
    target_link_options(dozerr-updater PRIVATE -static)
endif()
