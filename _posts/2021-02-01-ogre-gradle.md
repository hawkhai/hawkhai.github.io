---
layout: post
title: "编程 C++ -- OGRE Android gradle 构建配置文件"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程笔记", "Android"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


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

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-01-ogre-gradle.md.js" %}'></script></p>
