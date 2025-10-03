#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音标文件重命名脚本
将包含特殊字符的音标文件名重命名为数字编号，避免Jekyll构建错误
"""

import os
import shutil
import json
from pathlib import Path

# 音标到数字ID的映射
PHONETIC_MAPPING = {
    # 长元音
    'iː': '001',
    'ɜː': '002', 
    'ɑː': '003',
    'ɔː': '004',
    'uː': '005',
    
    # 短元音
    'ɪ': '006',
    'e': '007',
    'æ': '008',
    'ə': '009',
    'ʌ': '010',
    'ɒ': '011',
    'ʊ': '012',
    
    # 双元音
    'eɪ': '013',
    'aɪ': '014',
    'ɔɪ': '015',
    'əʊ': '016',
    'aʊ': '017',
    'ɪə': '018',
    'eə': '019',
    'ʊə': '020',
    
    # 清辅音
    'p': '021',
    't': '022',
    'k': '023',
    'f': '024',
    'θ': '025',
    's': '026',
    '∫': '027',
    'h': '028',
    't∫': '029',
    'ts': '030',
    'tr': '031',
    
    # 浊辅音
    'b': '032',
    'd': '033',
    'g': '034',
    'v': '035',
    'ð': '036',
    'z': '037',
    'ʒ': '038',
    'r': '039',
    'dʒ': '040',
    'dz': '041',
    'dr': '042',
    'm': '043',
    'n': '044',
    'ŋ': '045',
    'l': '046',
    'j': '047',
    'w': '048',
    
    # 字母发音
    'ks': '049',
    'tʃ': '050',
    'ʃ': '051'
}

def rename_files_in_directory(directory_path, mapping, dry_run=False):
    """
    重命名指定目录中的音频文件
    
    Args:
        directory_path: 目录路径
        mapping: 音标到数字ID的映射字典
        dry_run: 是否只是预览，不实际重命名
    
    Returns:
        tuple: (成功数量, 跳过数量, 错误列表)
    """
    directory = Path(directory_path)
    if not directory.exists():
        print(f"❌ 目录不存在: {directory_path}")
        return 0, 0, [f"目录不存在: {directory_path}"]
    
    print(f"📁 处理目录: {directory_path}")
    
    success_count = 0
    skip_count = 0
    errors = []
    
    # 获取所有mp3文件
    mp3_files = list(directory.glob("*.mp3"))
    
    for file_path in mp3_files:
        original_name = file_path.stem  # 不包含扩展名的文件名
        extension = file_path.suffix    # 扩展名
        
        if original_name in mapping:
            new_name = mapping[original_name]
            new_file_path = directory / f"{new_name}{extension}"
            
            if new_file_path.exists():
                print(f"  ⚠️  跳过: {file_path.name} -> {new_file_path.name} (目标文件已存在)")
                skip_count += 1
            else:
                if dry_run:
                    print(f"  🔍 预览: {file_path.name} -> {new_file_path.name}")
                else:
                    try:
                        file_path.rename(new_file_path)
                        print(f"  ✅ 重命名: {file_path.name} -> {new_file_path.name}")
                        success_count += 1
                    except Exception as e:
                        error_msg = f"重命名失败 {file_path.name}: {str(e)}"
                        print(f"  ❌ {error_msg}")
                        errors.append(error_msg)
        else:
            print(f"  ⚠️  未找到映射: {file_path.name}")
            skip_count += 1
    
    return success_count, skip_count, errors

def create_backup_mapping(mapping, output_file):
    """创建映射文件的备份"""
    # 创建反向映射
    reverse_mapping = {v: k for k, v in mapping.items()}
    
    backup_data = {
        "description": "音标文件重命名映射表",
        "created_by": "rename_phonetic_files.py",
        "phonetic_to_numeric": mapping,
        "numeric_to_phonetic": reverse_mapping
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(backup_data, f, ensure_ascii=False, indent=2)
    
    print(f"📄 映射表已保存到: {output_file}")

def main():
    """主函数"""
    print("🎵 音标文件重命名工具")
    print("=" * 50)
    
    # 获取脚本所在目录
    script_dir = Path(__file__).parent
    mp3_dir = script_dir / "mp3"
    yp_dir = script_dir / "yp"
    
    # 询问是否预览模式
    preview = input("是否先预览重命名操作？(y/n, 默认y): ").strip().lower()
    dry_run = preview != 'n'
    
    if dry_run:
        print("\n🔍 预览模式 - 不会实际重命名文件")
    else:
        print("\n🚀 执行模式 - 将实际重命名文件")
    
    print("-" * 50)
    
    total_success = 0
    total_skip = 0
    all_errors = []
    
    # 处理mp3目录
    if mp3_dir.exists():
        success, skip, errors = rename_files_in_directory(mp3_dir, PHONETIC_MAPPING, dry_run)
        total_success += success
        total_skip += skip
        all_errors.extend(errors)
    else:
        print(f"⚠️  mp3目录不存在: {mp3_dir}")
    
    print()
    
    # 处理yp目录
    if yp_dir.exists():
        success, skip, errors = rename_files_in_directory(yp_dir, PHONETIC_MAPPING, dry_run)
        total_success += success
        total_skip += skip
        all_errors.extend(errors)
    else:
        print(f"⚠️  yp目录不存在: {yp_dir}")
    
    # 创建映射备份文件
    if not dry_run:
        mapping_file = script_dir / "phonetic_mapping_backup.json"
        create_backup_mapping(PHONETIC_MAPPING, mapping_file)
    
    # 显示总结
    print("\n" + "=" * 50)
    print("📊 操作总结:")
    print(f"  ✅ 成功: {total_success} 个文件")
    print(f"  ⚠️  跳过: {total_skip} 个文件")
    print(f"  ❌ 错误: {len(all_errors)} 个")
    
    if all_errors:
        print("\n❌ 错误详情:")
        for error in all_errors:
            print(f"  - {error}")
    
    if dry_run and total_success > 0:
        print(f"\n💡 如需实际执行重命名，请重新运行脚本并选择 'n'")
    
    print("\n🎉 处理完成!")

if __name__ == "__main__":
    main()
