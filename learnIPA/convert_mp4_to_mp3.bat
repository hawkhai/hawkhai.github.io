@echo off
chcp 65001 >nul
echo 🎵 MP4 to MP3 转换工具 (批处理版本)
echo ================================================

REM 设置 FFmpeg 路径
set "FFMPEG_PATH=D:\佰阅科技\小白兔AI\ffmpeg.exe"

REM 检查 FFmpeg 文件是否存在
if not exist "%FFMPEG_PATH%" (
    echo ❌ FFmpeg 文件不存在: %FFMPEG_PATH%
    pause
    exit /b 1
)

REM 测试 FFmpeg 是否可用
"%FFMPEG_PATH%" -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ FFmpeg 无法运行: %FFMPEG_PATH%
    pause
    exit /b 1
)

echo ✅ FFmpeg 已找到: %FFMPEG_PATH%

REM 检查 tingclass 目录是否存在
if not exist "tingclass\" (
    echo ❌ tingclass 目录不存在
    pause
    exit /b 1
)

echo 📁 开始转换 tingclass 目录中的 MP4 文件...
echo.

set success_count=0
set skipped_count=0
set failed_count=0

REM 转换所有 MP4 文件
for %%f in (tingclass\*.mp4) do (
    set "input_file=%%f"
    set "output_file=tingclass\%%~nf.mp3"
    
    REM 检查是否已存在对应的 MP3 文件
    if exist "tingclass\%%~nf.mp3" (
        echo ⏭️  跳过 ^(已存在^): %%~nf.mp3
        set /a skipped_count+=1
    ) else (
        echo 🔄 转换: %%~nxf -^> %%~nf.mp3
        
        REM 使用 FFmpeg 转换
        "%FFMPEG_PATH%" -i "%%f" -vn -acodec mp3 -ab 192k -ar 44100 -y "tingclass\%%~nf.mp3" >nul 2>&1
        
        if %errorlevel% equ 0 (
            if exist "tingclass\%%~nf.mp3" (
                echo ✅ 转换成功: %%~nf.mp3
                set /a success_count+=1
            ) else (
                echo ❌ 转换失败: %%~nf.mp3 ^(文件未创建^)
                set /a failed_count+=1
            )
        ) else (
            echo ❌ 转换失败: %%~nf.mp3
            set /a failed_count+=1
        )
    )
)

echo.
echo ================================================
echo 📊 转换结果统计:
echo ✅ 成功: %success_count% 个文件
echo ⏭️  跳过: %skipped_count% 个文件  
echo ❌ 失败: %failed_count% 个文件

if %failed_count% equ 0 (
    echo.
    echo 🎉 所有文件转换完成！
) else (
    echo.
    echo ⚠️  有 %failed_count% 个文件转换失败
)

echo.
pause
