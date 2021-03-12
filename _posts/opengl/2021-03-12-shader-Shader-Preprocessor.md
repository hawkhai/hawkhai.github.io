---
layout: post
title: "图形学笔记 -- Shader Preprocessor"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

Shader 预处理器，从各个角度说来，都是必要的。

* [自制游戏引擎 - 5 Shader Preprocessor {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/34274224)
* [Wallpaper Engine Shader Preprocessor](https://wallpaper-engine.fandom.com/wiki/Shader_Preprocessor)
* [Predefined Shader preprocessor macros Unity](http://man.hubwiz.com/docset/Unity_3D.docset/Contents/Resources/Documents/docs.unity3d.com/Manual/SL-BuiltinMacros.html)
* [Using #ifdef in OpenGL* ES 2.0 Shaders](https://software.intel.com/content/www/us/en/develop/blogs/using-ifdef-in-opengl-es-20-shaders.html)
* 这个就是想要的，可惜是 JS 版本。[ShaderViewer -- reprocess and format the shader code. {% include relref_github.html %}](https://github.com/06wj/shaderViewer/tree/master)

* 支持 Engine 能够自定义插入 #define xxx。这样一来 Engine 可以有一系列可配置项，并根据用户的选择，在提交 Shader file
    到 GPU 之前，插入一些 Define Directives，做到一些流程控制。
* GLSL 并不支持 #include，但事实上 include 其他文件，比如自己的函数库之类的是一件被各大 Engine
    普遍支持的功能（对，然而 OpenGL 到现在为止 (450) 还都基本不支持）。
* 在插入自定义内容以后，行号会变，报错的地方会乱。所以需要在插入内容后，添加 #line 来为 Compiler 提供 hint。
* #define 需要插入在实际的 #verison 之后。划重点，实际的 #version。这意味着混在注释里的是不可以的。
* 同 2，只需要 include 真的 #include，注释里的需要忽略。
* Include 的文件里很可能还有 Include，所以需要继续 parse。这个时候，请再次小心第 1 点。
* Include 需要小心 Circular Dependencies
* Include 要维护 Include Directory 保证各种 Include 文件的路径都是合法的。（清完全参照 C/C++ 能支持的方式）

{% include image.html url="/assets/images/210312-shader-shader-preproces~18/the-preprocessor-transforms-a-shader-into-an-intermediate-representation-and-determines.png"
caption="The preprocessor transforms a shader into an intermediate representation and determines type information of its shader handlers for combination at runtime." %}

[A shader preprocessor based on fcpp (free c preprocessor). {% include relref_github.html %}](https://github.com/Chris-Zou/Preprocessor)
[OGRE 3.1.7 OpenGL GLSL](https://www.ogre3d.org/docs/manual18/manual_21.html)

{% include image.html url="/assets/images/210312-shader-shader-preproces~18/ogles2-shader-example-137862.png" %}
{% include image.html url="/assets/images/210312-shader-shader-preproces~18/ogles-ifdef-compile-shader-example-137862.png" %}
{% include image.html url="/assets/images/210312-shader-shader-preproces~18/tb1lkmzul1tbunjy0fjxxajyxxa-1170-1254.png_600x600.png" %}

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-12-shader-Shader-Preprocessor.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://zhuanlan.zhihu.com/p/34274224]({% include relref.html url="/backup/2021-03-12-shader-Shader-Preprocessor.md/zhuanlan.zhihu.com/b975adfe.html" %})
- [https://wallpaper-engine.fandom.com/wiki/Shader_Preprocessor]({% include relref.html url="/backup/2021-03-12-shader-Shader-Preprocessor.md/wallpaper-engine.fandom.com/0b3cdf8b.html" %})
- [http://man.hubwiz.com/docset/Unity_3D.docset/Contents/Resources/Documents/docs.unity3d.com/Manual/SL-BuiltinMacros.html]({% include relref.html url="/backup/2021-03-12-shader-Shader-Preprocessor.md/man.hubwiz.com/f60d6798.html" %})
- [https://software.intel.com/content/www/us/en/develop/blogs/using-ifdef-in-opengl-es-20-shaders.html]({% include relref.html url="/backup/2021-03-12-shader-Shader-Preprocessor.md/software.intel.com/66440f24.html" %})
- [https://github.com/06wj/shaderViewer/tree/master]({% include relref.html url="/backup/2021-03-12-shader-Shader-Preprocessor.md/github.com/d9d0b48e.html" %})
- [https://github.com/Chris-Zou/Preprocessor]({% include relref.html url="/backup/2021-03-12-shader-Shader-Preprocessor.md/github.com/6b6b7240.html" %})
- [https://www.ogre3d.org/docs/manual18/manual_21.html]({% include relref.html url="/backup/2021-03-12-shader-Shader-Preprocessor.md/www.ogre3d.org/0488937e.html" %})
