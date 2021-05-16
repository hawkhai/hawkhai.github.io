precision mediump float;

/* Uniforms */

uniform int uTextureUsage0; // 是否采用纹理
uniform int uTextureUsage1; // 是否采用纹理 2
uniform sampler2D uTextureUnit0; // 纹理单元
uniform sampler2D uTextureUnit1; // 纹理单元 2
uniform int uFogEnable; // 是否雾
uniform int uFogType; // 雾的类型
uniform vec4 uFogColor; // 雾的颜色
uniform float uFogStart; // 雾的开始 Linear FogType
uniform float uFogEnd; // 雾的结束 Linear FogType
uniform float uFogDensity; // 雾的密度

/* Varyings */

varying vec2 vTextureCoord0; // 纹理坐标
varying vec2 vTextureCoord1; // 纹理坐标 2
varying vec4 vVertexColor; // 顶点颜色
varying vec4 vSpecularColor; // 镜面反射颜色
varying float vFogCoord; // 雾的厚度，可以理解为深度。

float computeFog()
{
    const float LOG2 = 1.442695;
    float FogFactor = 0.0;

    if (uFogType == 0) // Exp
    {
        FogFactor = exp2(-uFogDensity * vFogCoord * LOG2);
    }
    else if (uFogType == 1) // Linear
    {
        float Scale = 1.0 / (uFogEnd - uFogStart);
        FogFactor = (uFogEnd - vFogCoord) * Scale;
    }
    else if (uFogType == 2) // Exp2
    {
        FogFactor = exp2(-uFogDensity * uFogDensity * vFogCoord * vFogCoord * LOG2);
    }

    FogFactor = clamp(FogFactor, 0.0, 1.0);

    return FogFactor;
}

void main()
{
    vec4 Color0 = vec4(1.0, 1.0, 1.0, 1.0);
    vec4 Color1 = vec4(1.0, 1.0, 1.0, 1.0);

    if (bool(uTextureUsage0))
        Color0 = texture2D(uTextureUnit0, vTextureCoord0);

    if (bool(uTextureUsage1))
        Color1 = texture2D(uTextureUnit1, vTextureCoord1);

    vec4 FinalColor = (Color0 * Color1) * vVertexColor + vSpecularColor;

    if (bool(uFogEnable))
    {
        float FogFactor = computeFog();
        vec4 FogColor = uFogColor;
        FogColor.a = 1.0;
        FinalColor = mix(FogColor, FinalColor, FogFactor);
    }

    gl_FragColor = FinalColor;
}
