---
layout: post
title: "编程配置 -- OGRE Android gradle & CMake 构建配置文件"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "Android", "Ogre3D"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

这玩意儿没有示例，凭感觉配置出来的，最后居然全部能跑，呵呵。
比较麻烦的一个重要原因就是：改几行十秒钟，构建验证一小时。


## ogrecore

```gradle
apply plugin: 'com.android.library'

android {

    defaultConfig {

        externalNativeBuild {
            cmake {
                // -frtti 开启 RTTI 的支持 dynamic_cast 和 typeid 需要用到。
                // -fexceptions 标记可以开启异常控制。
                cppFlags "-std=c++11 -frtti -fexceptions"
                arguments "-DANDROID_STL=c++_static",
                        "-DANDROID_ARM_NEON=TRUE", // 使用 NEON 对代码进行优化
                        "-DOGRE_BUILD_COMPONENT_JAVA=TRUE",
                        "-DOGRE_BUILD_ANDROID_JNI_SAMPLE=TRUE",
                        "-DOGRE_BUILD_SAMPLES=FALSE",
                        "-DOGRE_CONFIG_THREADS=0"
            }
        }
        ndk {
            abiFilters "armeabi-v7a"
        }
    }

    externalNativeBuild {
        cmake {
            path "ogre/CMakeLists.txt"
            version "3.10.2"
        }
    }
}
```


## ogreapp

```gradle
apply plugin: 'com.android.library'

android {
    defaultConfig {

        externalNativeBuild {
            cmake {
                cppFlags "-std=c++11 -frtti -fexceptions"
                arguments "-DANDROID_STL=c++_static",
                        "-DANDROID_ARM_NEON=TRUE"
            }
        }
        ndk {
            abiFilters "armeabi-v7a"
        }
    }

    externalNativeBuild {
        cmake {
            path "src/main/cpp/CMakeLists.txt"
            version "3.10.2"
        }
    }
}

dependencies {
    // implementation project(":ogrecore")
}
```


### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.4.1)

set(JSONCPP_WITH_TESTS 0)
set(JSONCPP_WITH_POST_BUILD_UNITTEST 0)
add_subdirectory(jsoncpp)
set(json-lib ${CMAKE_CURRENT_BINARY_DIR}/jsoncpp/src/lib_json/libjsoncpp.a)

#add_definitions(-DINCLUDE_RTSHADER_SYSTEM)
#add_definitions(-DOGRE_STATIC_LIB)
#add_definitions(-DOGRE_BUILD_COMPONENT_RTSHADERSYSTEM)

add_library( # Sets the name of the library.
        magicview

        # Sets the library as a shared library.
        SHARED

        Browser/src/GestureDetector.cpp
        Browser/src/DynTex.cpp
        Browser/src/BgSample.cpp
        Browser/src/ScreenshotManager.cpp
        Browser/src/WaterMesh.cpp

        External/ExternalResource.cpp

        data/Effect.cpp
        data/Config.cpp

        native-func.cpp
        ogre-utils.cpp

        # Provides a relative path to your source file(s).
        native-lib.cpp)

find_library( # Sets the name of the path variable.
        log-lib

        # Specifies the name of the NDK library that
        # you want CMake to locate.
        log)

include_directories(./)
include_directories(./libgdx)
include_directories(./External)
include_directories(./Browser/include)
include_directories(./jsoncpp/include)
#include_directories(./opencv/include)
include_directories(${CMAKE_CURRENT_BINARY_DIR}/jsoncpp/include/json)

SET(OGRE_ROOT_DIR "${CMAKE_SOURCE_DIR}/../../../../ogrecore")

get_filename_component(OGRE_ROOT_DIR "${OGRE_ROOT_DIR}" ABSOLUTE)

SET(OGRE_CODE_DIR "${OGRE_ROOT_DIR}/ogre")
SET(OGRE_MAKE_DIR "${OGRE_ROOT_DIR}/.externalNativeBuild/cmake/${CMAKE_BUILD_TYPE}/${ANDROID_ABI}")
if (NOT EXISTS "${OGRE_MAKE_DIR}/")
    SET(OGRE_MAKE_DIR "${OGRE_ROOT_DIR}/ogrejni/${CMAKE_BUILD_TYPE}/${ANDROID_ABI}")
endif()
if (NOT EXISTS "${OGRE_MAKE_DIR}/")
    SET(OGRE_MAKE_DIR "${OGRE_ROOT_DIR}/ogrejni/Release/${ANDROID_ABI}")
endif()

message(WARNING "OGRE ${CMAKE_BUILD_TYPE} build lib link dir is: ${OGRE_MAKE_DIR}")
file(WRITE ./cmake_${CMAKE_BUILD_TYPE}_log.txt "OGRE build lib link dir is:\n${OGRE_MAKE_DIR}\n\n")

include_directories(${OGRE_MAKE_DIR}/include)
include_directories(${OGRE_CODE_DIR}/OgreMain/include)
include_directories(${OGRE_CODE_DIR}/Components/Bites/include)
include_directories(${OGRE_CODE_DIR}/Components/Overlay/include)
include_directories(${OGRE_CODE_DIR}/Components/RTShaderSystem/include)
include_directories(${OGRE_CODE_DIR}/PlugIns/ParticleFX/include)
include_directories(${OGRE_CODE_DIR}/PlugIns/ParticleUniverse/include)
include_directories(${OGRE_CODE_DIR}/PlugIns/OctreeSceneManager/include)
include_directories(${OGRE_CODE_DIR}/RenderSystems/GLES2/include)
include_directories(${OGRE_CODE_DIR}/RenderSystems/GLSupport/include)
include_directories(${OGRE_CODE_DIR}/RenderSystems/GLSupport/include/GLSL)

# Specifies libraries CMake should link to your target library. You
# can link multiple libraries, such as libraries you define in this
# build script, prebuilt third-party libraries, or system libraries.
if (${CMAKE_BUILD_TYPE} STREQUAL "Debug" OR ${CMAKE_BUILD_TYPE} STREQUAL "debug")
    set(FREETYPE_LIBRARY "${OGRE_MAKE_DIR}/Dependencies/lib/libfreetyped.a")
else()
    set(FREETYPE_LIBRARY "${OGRE_MAKE_DIR}/Dependencies/lib/libfreetype.a")
endif()
if (NOT EXISTS "${FREETYPE_LIBRARY}")
    set(FREETYPE_LIBRARY "${OGRE_MAKE_DIR}/Dependencies/lib/libfreetype.a")
endif()

target_link_libraries( # Specifies the target library.
        magicview

        ${OGRE_MAKE_DIR}/lib/libOgreBitesStatic.a
        ${OGRE_MAKE_DIR}/lib/libOgreOverlayStatic.a
        ${OGRE_MAKE_DIR}/lib/libOgreRTShaderSystemStatic.a
        ${OGRE_MAKE_DIR}/lib/libOgreMainStatic.a
        ${OGRE_MAKE_DIR}/lib/libPlugin_ParticleFXStatic.a
        ${OGRE_MAKE_DIR}/lib/libPlugin_ParticleUniverseStatic.a
        ${OGRE_MAKE_DIR}/lib/libPlugin_OctreeSceneManagerStatic.a
        ${OGRE_MAKE_DIR}/lib/libRenderSystem_GLES2Static.a

        ${OGRE_MAKE_DIR}/lib/libcpufeatures.a
        "${FREETYPE_LIBRARY}"
        ${OGRE_MAKE_DIR}/lib/libOgreGLSupportStatic.a

        ${OGRE_MAKE_DIR}/lib/libPlugin_DotSceneStatic.a
        ${OGRE_MAKE_DIR}/Dependencies/lib/libpugixml.a
        ${OGRE_MAKE_DIR}/lib/libOgreTerrainStatic.a
        ${OGRE_MAKE_DIR}/lib/libOgrePagingStatic.a
        ${OGRE_MAKE_DIR}/lib/libCodec_STBIStatic.a
        ${OGRE_MAKE_DIR}/Dependencies/lib/libzzip.a

        -ljnigraphics

        libz.a
        ${json-lib}
        -lEGL -landroid -llog -lGLESv2 -ldl -latomic -lm
        ${log-lib})
```


### ParticleUniverse

```cmake
file(GLOB HEADER_FILES "${CMAKE_CURRENT_SOURCE_DIR}/include/*.h")
list(APPEND HEADER_FILES ${PROJECT_BINARY_DIR}/include/ParticleUniversePrerequisites.h)
file(GLOB SOURCE_FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp"
        "${CMAKE_CURRENT_SOURCE_DIR}/src/*/*.cpp")

add_library(Plugin_ParticleUniverse ${OGRE_LIB_TYPE} ${HEADER_FILES} ${SOURCE_FILES})
target_link_libraries(Plugin_ParticleUniverse OgreMain)

target_include_directories(Plugin_ParticleUniverse PUBLIC
        "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
        $<INSTALL_INTERFACE:include/OGRE/Plugins/ParticleUniverse>)

generate_export_header(Plugin_ParticleUniverse
        EXPORT_MACRO_NAME _ParticleUniverseExport
        EXPORT_FILE_NAME ${PROJECT_BINARY_DIR}/include/ParticleUniversePrerequisites.h)

ogre_config_framework(Plugin_ParticleUniverse)

ogre_config_plugin(Plugin_ParticleUniverse)
install(FILES ${HEADER_FILES} DESTINATION include/OGRE/Plugins/ParticleUniverse)
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-01-ogre-gradle.md.js" %}'></script></p>
