---
layout: post
title: "Irrlicht 3D 笔记 -- OpenGL ES 2.x Driver 源码剖析 2D 部分"
author:
location: "珠海"
categories: ["Irrlicht"]
tags: ["Irrlicht"]
toc: true
toclistyle: none
comments:
visibility:
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
cluster: "Irrlicht OpenGL-ES2 Driver"
---


## COGLES2Renderer2D.vsh

```glsl
/* Attributes */

attribute vec4 inVertexPosition;
attribute vec4 inVertexColor;
attribute vec2 inTexCoord0;

/* Uniforms */

uniform float uThickness;

/* Varyings */

varying vec2 vTextureCoord;
varying vec4 vVertexColor;

void main()
{
    gl_Position = inVertexPosition;
    gl_PointSize = uThickness;
    vTextureCoord = inTexCoord0;
    vVertexColor = inVertexColor.bgra;
}

```


## COGLES2Renderer2D.fsh

```glsl
precision mediump float;

/* Uniforms */

uniform int uTextureUsage;
uniform sampler2D uTextureUnit;

/* Varyings */

varying vec2 vTextureCoord;
varying vec4 vVertexColor;

void main()
{
    vec4 Color = vVertexColor;

    if (bool(uTextureUsage))
        Color *= texture2D(uTextureUnit, vTextureCoord);

    gl_FragColor = Color;
}

```


## COGLES2Renderer2D_noTex.fsh

```glsl
precision mediump float;

/* Varyings */
varying vec4 vVertexColor;

void main()
{
    gl_FragColor = vVertexColor;
}

```
