#define MAX_LIGHTS 2 // 最多两个光源

precision mediump float;

/* Uniforms */

uniform float uFactor; // 纹理颜色的乘积参数
uniform sampler2D uTextureUnit0; // 纹理单元
uniform sampler2D uTextureUnit1; // 纹理单元 2
uniform int uFogEnable; // 是否雾
uniform int uFogType; // 雾的类型
uniform vec4 uFogColor; // 雾的颜色
uniform float uFogStart; // 雾的开始 Linear FogType
uniform float uFogEnd; // 雾的结束 Linear FogType
uniform float uFogDensity; // 雾的密度

/* Varyings */

varying vec2 vTexCoord; // 纹理坐标
varying vec3 vEyeVector; // 相机向量
varying vec3 vLightVector[MAX_LIGHTS]; // 光源向量
varying vec4 vLightColor[MAX_LIGHTS]; // 光源颜色
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
    vec4 TempFetch = texture2D(uTextureUnit1, vTexCoord) *  2.0 - 1.0;
    TempFetch *= uFactor;

    vec3 EyeVector = normalize(vEyeVector);
    vec2 TexCoord = EyeVector.xy * TempFetch.w + vTexCoord;

    vec4 Color  = texture2D(uTextureUnit0, TexCoord);
    vec3 Normal = texture2D(uTextureUnit1, TexCoord).xyz *  2.0 - 1.0;

    vec4 FinalColor = vec4(0.0, 0.0, 0.0, 0.0);

    for (int i = 0; i < int(MAX_LIGHTS); i++)
    {
        vec3 LightVector = normalize(vLightVector[i]);

        float Lambert = max(dot(LightVector, Normal), 0.0);
        FinalColor += vec4(Lambert) * vLightColor[i];
    }

    FinalColor *= Color;
    FinalColor.w = vLightColor[0].w;

    if (bool(uFogEnable))
    {
        float FogFactor = computeFog();
        vec4 FogColor = uFogColor;
        FogColor.a = 1.0;
        FinalColor = mix(FogColor, FinalColor, FogFactor);
    }

    gl_FragColor = FinalColor;
}
