/* Attributes */

attribute vec4 inVertexPosition; // 顶点坐标
attribute vec4 inVertexColor; // 顶点颜色
attribute vec2 inTexCoord0; // 纹理坐标

/* Uniforms */

uniform float uThickness; // 绘制的粗细。

/* Varyings */

varying vec2 vTextureCoord; // 纹理坐标
varying vec4 vVertexColor; // 顶点颜色

void main()
{
    gl_Position = inVertexPosition;
    gl_PointSize = uThickness;
    vTextureCoord = inTexCoord0;
    vVertexColor = inVertexColor.bgra;
}
