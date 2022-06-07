precision mediump float;

/* Uniforms */

uniform int uTextureUsage; // 是否采用纹理。
uniform sampler2D uTextureUnit; // 纹理单元。

/* Varyings */

varying vec2 vTextureCoord; // 纹理坐标
varying vec4 vVertexColor; // 顶点颜色

void main()
{
    vec4 Color = vVertexColor;

    if (bool(uTextureUsage)) // 如果采用纹理，就把纹理 乘上去。
        Color *= texture2D(uTextureUnit, vTextureCoord);

    gl_FragColor = Color;
}
