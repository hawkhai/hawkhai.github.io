---
layout: post
title: "图形学笔记 -- OpenGL 拷贝纹理的两种方式 & Texture storage format"
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


## TEXTURE_FORMAT.md

**Texture storage format**
Wallpaper engine uses a custom texture storage format converted by resourcecompiler.exe


### Header

| Information | Size | Default value |
|---|---|---|
| __File type indicator__ | 8 bytes | TEXV0005 |
| __Padding__ | 1 byte | Null terminator for string |
| __Extra file type indicator?__ | 8 bytes | TEXI0001 |
| __Padding__ | 1 byte | Null terminator for string |
| __Texture type__ | 1 byte | 4 => DXT5? 0 => JPEG? |
| __Unknown data__ | 15 bytes | To be reversed |
| __Width__ | 4 bytes | Image's width |
| __Height__ | 4 bytes | Image's height |
| __Unknown data__ | 5 bytes | To be reversed |
| __Container version__ | 8 bytes | TEXB0003 |
| __Padding__ | 1 byte | Null terminator for string |
| __Unknown data__ | 8 bytes | To be reversed |
| __Mip map levels__ | 4 bytes | The number of mipmaps stored for this texture |
| __Mipmap entry__ | x bytes | See Mipmap entries |


### Mipmap entries

| Information | Size | Default value |
|---|---|---|
| __Width__ | 4 bytes | Mipmap's entry width |
| __Height__| 4 bytes | Mipmap's entry height |
| __Compression flag__ | 4 bytes | Indicates if the content is compressed or not |
| __Next image size__ | 4 bytes | Image block size (uncompressed) |
| __Next image size__ | 4 bytes | Image block size (compressed) |
| __Mipmap pixels__ | x bytes | Actual bitmap data in the format specified |


## fakehookDebug.cpp

```cpp
GLuint GetDebugTextureId() {
    static GLuint texture = 0;
    if (texture != 0) {
        return texture;
    }
    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);
    if (true) {
        GLubyte data[] = {
            255, 0, 0, 155,
            0, 255, 0, 155,
            0, 0, 255, 155,
            255, 255, 255, 155 };
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

        GLsizei width = 2;
        GLsizei height = 2;
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
        glGenerateMipmap(GL_TEXTURE_2D);
    }
    glBindTexture(GL_TEXTURE_2D, 0);
    return texture;
}
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-07-opengl-tex-copy.md.js" %}'></script></p>
