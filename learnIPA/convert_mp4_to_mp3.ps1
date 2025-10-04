# MP4 to MP3 转换脚本 (PowerShell 版本)
# 将 tingclass 文件夹中的所有 MP4 文件转换为 MP3 格式

param(
    [string]$Quality = "192k",
    [switch]$Force = $false
)

# 设置控制台编码为 UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# FFmpeg 可执行文件路径
$FFmpegPath = "D:\佰阅科技\小白兔AI\ffmpeg.exe"

Write-Host "🎵 MP4 to MP3 转换工具 (PowerShell 版本)" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Gray

# 检查 FFmpeg 是否可用
function Test-FFmpeg {
    try {
        if (-not (Test-Path $FFmpegPath)) {
            Write-Host "❌ FFmpeg 文件不存在: $FFmpegPath" -ForegroundColor Red
            return $false
        }
        
        $null = & $FFmpegPath -version 2>$null
        Write-Host "✅ FFmpeg 已找到: $FFmpegPath" -ForegroundColor Green
        return $true
    }
    catch {
        Write-Host "❌ FFmpeg 无法运行: $FFmpegPath" -ForegroundColor Red
        Write-Host "错误: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# 转换单个文件
function Convert-Mp4ToMp3 {
    param(
        [string]$InputFile,
        [string]$OutputFile,
        [string]$Quality = "192k"
    )
    
    try {
        Write-Host "🔄 转换: $(Split-Path $InputFile -Leaf) -> $(Split-Path $OutputFile -Leaf)" -ForegroundColor Yellow
        
        $arguments = @(
            '-i', $InputFile,
            '-vn',
            '-acodec', 'mp3',
            '-ab', $Quality,
            '-ar', '44100',
            '-y',
            $OutputFile
        )
        
        $process = Start-Process -FilePath $FFmpegPath -ArgumentList $arguments -Wait -NoNewWindow -PassThru -RedirectStandardError 'NUL'
        
        if ($process.ExitCode -eq 0 -and (Test-Path $OutputFile) -and (Get-Item $OutputFile).Length -gt 0) {
            Write-Host "✅ 转换成功: $(Split-Path $OutputFile -Leaf)" -ForegroundColor Green
            return $true
        }
        else {
            Write-Host "❌ 转换失败: $(Split-Path $OutputFile -Leaf)" -ForegroundColor Red
            return $false
        }
    }
    catch {
        Write-Host "❌ 转换出错: $(Split-Path $InputFile -Leaf)" -ForegroundColor Red
        Write-Host "错误: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# 主函数
function Main {
    # 检查 FFmpeg
    if (-not (Test-FFmpeg)) {
        return 1
    }
    
    # 设置路径
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
    $tingclassDir = Join-Path $scriptDir "tingclass"
    
    if (-not (Test-Path $tingclassDir)) {
        Write-Host "❌ 目录不存在: $tingclassDir" -ForegroundColor Red
        return 1
    }
    
    # 查找所有 MP4 文件
    $mp4Files = Get-ChildItem -Path $tingclassDir -Filter "*.mp4" | Sort-Object Name
    
    if ($mp4Files.Count -eq 0) {
        Write-Host "❌ 在 $tingclassDir 中未找到 MP4 文件" -ForegroundColor Red
        return 1
    }
    
    Write-Host "📁 找到 $($mp4Files.Count) 个 MP4 文件" -ForegroundColor Cyan
    
    # 转换统计
    $successCount = 0
    $failedCount = 0
    $skippedCount = 0
    
    # 转换每个文件
    foreach ($mp4File in $mp4Files) {
        $mp3File = Join-Path $tingclassDir ($mp4File.BaseName + ".mp3")
        
        # 检查是否已存在 MP3 文件
        if ((Test-Path $mp3File) -and -not $Force) {
            Write-Host "⏭️  跳过 (已存在): $($mp4File.BaseName).mp3" -ForegroundColor Gray
            $skippedCount++
            continue
        }
        
        # 转换文件
        if (Convert-Mp4ToMp3 -InputFile $mp4File.FullName -OutputFile $mp3File -Quality $Quality) {
            $successCount++
        }
        else {
            $failedCount++
        }
    }
    
    # 显示结果统计
    Write-Host ""
    Write-Host "=" * 50 -ForegroundColor Gray
    Write-Host "📊 转换结果统计:" -ForegroundColor Cyan
    Write-Host "✅ 成功: $successCount 个文件" -ForegroundColor Green
    Write-Host "⏭️  跳过: $skippedCount 个文件" -ForegroundColor Gray
    Write-Host "❌ 失败: $failedCount 个文件" -ForegroundColor Red
    Write-Host "📁 总计: $($mp4Files.Count) 个文件" -ForegroundColor Cyan
    
    if ($failedCount -eq 0) {
        Write-Host ""
        Write-Host "🎉 所有文件转换完成！" -ForegroundColor Green
        return 0
    }
    else {
        Write-Host ""
        Write-Host "⚠️  有 $failedCount 个文件转换失败" -ForegroundColor Yellow
        return 1
    }
}

# 执行主函数
try {
    $exitCode = Main
    exit $exitCode
}
catch {
    Write-Host ""
    Write-Host "❌ 程序出错: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
