#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MP4 to MP3 转换脚本
将 tingclass 文件夹中的所有 MP4 文件转换为 MP3 格式
"""

import os
import subprocess
import sys
from pathlib import Path

# 设置控制台编码
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

# FFmpeg 可执行文件路径
FFMPEG_PATH = r"D:\佰阅科技\小白兔AI\ffmpeg.exe"

def check_ffmpeg():
    """检查 FFmpeg 是否可用"""
    try:
        if not os.path.exists(FFMPEG_PATH):
            print(f"❌ FFmpeg 文件不存在: {FFMPEG_PATH}")
            return False
            
        result = subprocess.run([FFMPEG_PATH, '-version'], 
                              capture_output=True, text=True, check=True)
        print(f"✅ FFmpeg 已找到: {FFMPEG_PATH}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ FFmpeg 无法运行: {FFMPEG_PATH}")
        print(f"错误: {str(e)}")
        return False

def convert_mp4_to_mp3(input_file, output_file, quality='192k'):
    """
    使用 FFmpeg 将 MP4 转换为 MP3
    
    Args:
        input_file: 输入的 MP4 文件路径
        output_file: 输出的 MP3 文件路径
        quality: 音频质量 (默认 192k)
    """
    try:
        cmd = [
            FFMPEG_PATH,
            '-i', str(input_file),
            '-vn',  # 不处理视频流
            '-acodec', 'mp3',  # 使用 MP3 编码器
            '-ab', quality,  # 音频比特率
            '-ar', '44100',  # 采样率
            '-y',  # 覆盖输出文件
            str(output_file)
        ]
        
        print(f"🔄 转换: {input_file.name} -> {output_file.name}")
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # 检查输出文件是否创建成功
        if output_file.exists() and output_file.stat().st_size > 0:
            print(f"✅ 转换成功: {output_file.name}")
            return True
        else:
            print(f"❌ 转换失败: {output_file.name} (文件未创建或为空)")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ 转换失败: {input_file.name}")
        print(f"错误信息: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ 转换出错: {input_file.name}")
        print(f"错误: {str(e)}")
        return False

def main():
    """主函数"""
    print("🎵 MP4 to MP3 转换工具")
    print("=" * 50)
    
    # 检查 FFmpeg
    if not check_ffmpeg():
        return 1
    
    # 设置路径
    script_dir = Path(__file__).parent
    tingclass_dir = script_dir / 'tingclass'
    
    if not tingclass_dir.exists():
        print(f"❌ 目录不存在: {tingclass_dir}")
        return 1
    
    # 查找所有 MP4 文件
    mp4_files = list(tingclass_dir.glob('*.mp4'))
    
    if not mp4_files:
        print(f"❌ 在 {tingclass_dir} 中未找到 MP4 文件")
        return 1
    
    print(f"📁 找到 {len(mp4_files)} 个 MP4 文件")
    
    # 创建输出目录（如果不存在）
    output_dir = tingclass_dir
    
    # 转换统计
    success_count = 0
    failed_count = 0
    skipped_count = 0
    
    # 转换每个文件
    for mp4_file in sorted(mp4_files):
        # 生成输出文件名
        mp3_file = output_dir / (mp4_file.stem + '.mp3')
        
        # 检查是否已存在 MP3 文件
        if mp3_file.exists():
            print(f"⏭️  跳过 (已存在): {mp3_file.name}")
            skipped_count += 1
            continue
        
        # 转换文件
        if convert_mp4_to_mp3(mp4_file, mp3_file):
            success_count += 1
        else:
            failed_count += 1
    
    # 显示结果统计
    print("\n" + "=" * 50)
    print("📊 转换结果统计:")
    print(f"✅ 成功: {success_count} 个文件")
    print(f"⏭️  跳过: {skipped_count} 个文件")
    print(f"❌ 失败: {failed_count} 个文件")
    print(f"📁 总计: {len(mp4_files)} 个文件")
    
    if failed_count == 0:
        print("\n🎉 所有文件转换完成！")
        return 0
    else:
        print(f"\n⚠️  有 {failed_count} 个文件转换失败")
        return 1

if __name__ == '__main__':
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⏹️  用户中断操作")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 程序出错: {str(e)}")
        sys.exit(1)
