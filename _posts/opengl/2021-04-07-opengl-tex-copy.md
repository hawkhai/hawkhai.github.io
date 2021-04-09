---
layout: post
title: "图形学笔记 -- OpenGL 拷贝纹理的两种方式"
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

一种是直观的使用 glGetTexImage，然后获取数据到内存再贴上去，这种方法很慢。

另一种是使用 FBO，将纹理附加到 FBO，然后用 glCopyTexSubImage2D，不涉及跟内存交换数据，速度飞快。

方法一：获取纹理再拷贝

```cpp
unsigned char * data = new unsigned char[normal_texture.width*normal_texture.height*4];

glBindTexture(GL_TEXTURE_2D, src_id); // 绑定 src_id
glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA, GL_UNSIGNED_BYTE, data); // 下载到 data

glBindTexture(GL_TEXTURE_2D, dest_id); // 绑定 dest_id
glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE, data); // 上传

glBindTexture(GL_TEXTURE_2D, 0);
```

第二种方法：FBO 拷贝

```cpp
GLuint fbo;
glGenFramebuffers(1, &fbo);
// bind the FBO
glBindFramebuffer(GL_READ_FRAMEBUFFER, fbo); // 绑定 FBO
    // attach the source texture to the fbo
    glFramebufferTexture2D(GL_READ_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, src_id, 0); // 绑定纹理到 FBO
    // bind the destination texture
    glBindTexture(GL_TEXTURE_2D, dest_id); // 绑定 dest_id
        // copy from framebuffer (here, the FBO!) to the bound texture
        glCopyTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 0, 0, width, height); // 从 FBO 直接拷贝到 dest_id
    glBindTexture(GL_TEXTURE_2D, 0);
// unbind the FBO
glBindFramebuffer(GL_FRAMEBUFFER, 0);
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relrefx.html url="/assets/reviewjs/blogs/2021-04-07-opengl-tex-copy.md.js" %}'></script></p>
