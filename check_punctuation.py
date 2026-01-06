#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
检查中文行中是否包含英文符号
规则：如果一行包含中文，则不应该包含英文符号（ASCII < 255的非字母数字字符）
"""

import re, sys
from pathlib import Path

REPLACE = "replace" in sys.argv

def has_chinese(text):
    """检查文本是否包含中文字符"""
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def fix_quotes_in_line(line):
    """
    修复一行中的英文双引号
    如果包含偶数个双引号且包含中文，替换为中文引号并移除内侧空格
    返回：(修改后的行, 是否修改)
    """
    # 统计双引号数量
    quote_count = line.count('"')

    # 如果不是偶数个或没有双引号，不处理
    if quote_count == 0 or quote_count % 2 != 0:
        return line, False

    # 如果没有中文，不处理
    if not has_chinese(line):
        return line, False

    # 替换成对的双引号
    result = []
    in_quote = False
    i = 0

    while i < len(line):
        if line[i] == '"':
            if not in_quote:
                # 开始引号
                result.append('"')
                in_quote = True
                # 跳过后面的空格
                i += 1
                while i < len(line) and line[i] == ' ':
                    i += 1
                continue
            else:
                # 结束引号
                # 移除前面的空格
                while result and result[-1] == ' ':
                    result.pop()
                result.append('"')
                in_quote = False
        else:
            result.append(line[i])
        i += 1

    new_line = ''.join(result)
    return new_line, (new_line != line)

def is_chinese_char(char):
    """检查是否是中文字符或中文标点"""
    # 中文字符范围
    if '\u4e00' <= char <= '\u9fff':
        return True
    # 中文标点符号范围
    if '\u3000' <= char <= '\u303f':  # CJK 符号和标点
        return True
    if '\uff00' <= char <= '\uffef':  # 全角ASCII、全角标点
        return True
    return False

def find_english_punctuation(text):
    """
    查找英文符号（小于255的非英文字母数字）
    只报告前后有空格且左右都有中文/中文符号的符号
    返回：[(符号, 位置), ...]
    """
    punctuations = []
    for i, char in enumerate(text):
        # ASCII < 255
        if ord(char) < 255:
            # 不是字母和数字
            if not char.isalnum():
                # 不是空白字符（空格、制表符等）
                if not char.isspace():
                    # 忽略星号和间隔号
                    if char not in ['*', '·']:
                        # 检查前后是否有空格
                        has_space_before = (i == 0 or text[i-1].isspace())
                        has_space_after = (i == len(text)-1 or text[i+1].isspace())

                        # 只有前后至少有一个空格时才继续检查
                        if has_space_before or has_space_after:
                            # 查找左边第一个非空格字符
                            left_chinese = False
                            for j in range(i-1, -1, -1):
                                if not text[j].isspace():
                                    left_chinese = is_chinese_char(text[j])
                                    break

                            # 查找右边第一个非空格字符
                            right_chinese = False
                            for j in range(i+1, len(text)):
                                if not text[j].isspace():
                                    right_chinese = is_chinese_char(text[j])
                                    break

                            # 左右都必须是中文或中文符号
                            if left_chinese and right_chinese:
                                punctuations.append((char, i))
    return punctuations

def check_file(file_path):
    """
    检查单个文件
    如果 REPLACE=True，则修改文件；否则只检查
    返回：(问题行列表, 修改行列表)
    """
    issues = []
    modified_lines_info = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 追踪是否在 YAML front matter 中
        in_front_matter = False
        front_matter_count = 0

        new_lines = []  # 用于存储修改后的行

        for line_num, line in enumerate(lines, 1):
            # 保留原始行（包括换行符）
            original_line = line
            # 去掉行尾换行符用于检查
            line_content = line.rstrip('\n\r')
            line_ending = line[len(line_content):]  # 保存换行符

            # 检查是否是 front matter 分隔符
            if line_content.strip() == '---':
                front_matter_count += 1
                if front_matter_count == 1:
                    in_front_matter = True
                elif front_matter_count == 2:
                    in_front_matter = False
                new_lines.append(original_line)
                continue

            # 跳过 front matter 区域
            if in_front_matter:
                new_lines.append(original_line)
                continue

            # 跳过空行
            if not line_content.strip():
                new_lines.append(original_line)
                continue

            # 跳过包含"参考资料快照"的行
            if "参考资料快照" in line_content:
                new_lines.append(original_line)
                continue

            # 如果行包含中文
            if has_chinese(line_content):
                # 如果是替换模式，尝试修复引号
                if REPLACE:
                    fixed_line, was_modified = fix_quotes_in_line(line_content)
                    if was_modified:
                        modified_lines_info.append({
                            'line_num': line_num,
                            'original': line_content,
                            'modified': fixed_line
                        })
                        new_lines.append(fixed_line + line_ending)
                    else:
                        new_lines.append(original_line)
                else:
                    new_lines.append(original_line)

                # 检查是否还有问题
                check_content = fixed_line if REPLACE and was_modified else line_content
                eng_puncts = find_english_punctuation(check_content)

                if eng_puncts:
                    issues.append({
                        'line_num': line_num,
                        'content': check_content,
                        'punctuations': eng_puncts
                    })
            else:
                new_lines.append(original_line)

        # 如果是替换模式且有修改，写回文件
        if REPLACE and modified_lines_info:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)

    except Exception as e:
        print(f"✗ 错误读取文件 {file_path}: {e}")
        return None, None

    return issues, modified_lines_info

def main(file_paths):
    """
    主函数：检查所有文件
    """
    total_issues = 0
    total_modified = 0

    print("=" * 80)
    if REPLACE:
        print("中英文标点符号自动修复模式")
        print("将替换中文行中的英文双引号为中文引号，并移除内侧空格")
    else:
        print("中英文标点符号混用检查")
        print("规则：中文行中不应出现英文符号（ASCII < 255 的非字母数字字符）")
        print("提示：使用 'python check_punctuation.py replace' 启用自动修复")
    print("=" * 80)
    print()

    for file_path_str in file_paths:
        file_path = Path(file_path_str)

        if not file_path.exists():
            print(f"✗ 文件不存在: {file_path}")
            print()
            continue

        print(f"📄 {'修复' if REPLACE else '检查'}文件: {file_path.name}")
        print(f"   路径: {file_path}")

        issues, modified_lines = check_file(file_path)

        if issues is None:
            print()
            continue

        # 显示修改信息
        if REPLACE and modified_lines:
            print(f"   ✏️  已修改 {len(modified_lines)} 行:")
            for mod in modified_lines:
                print(f"   【行 {mod['line_num']}】")
                print(f"   原文: {mod['original']}")
                print(f"   修改: {mod['modified']}")
                print()
            total_modified += len(modified_lines)

        # 显示剩余问题
        if not issues:
            print("   ✓ 无问题" if not REPLACE else "   ✓ 修复后无问题")
        else:
            print(f"   {'⚠️  仍有' if REPLACE else '❌ 发现'} {len(issues)} 个问题行:")
            print()

            for issue in issues:
                line_num = issue['line_num']
                content = issue['content']
                puncts = issue['punctuations']

                # 显示行号和内容
                print(f"   【行 {line_num}】")
                print(f"   {content}")

                # 显示问题符号
                punct_info = ', '.join([f"'{p[0]}'(位置{p[1]})" for p in puncts])
                print(f"   问题符号: {punct_info}")
                print()

            total_issues += len(issues)

        print("-" * 80)
        print()

    print("=" * 80)
    if REPLACE:
        print(f"修复完成：")
        print(f"  已修改: {total_modified} 行")
        print(f"  剩余问题: {total_issues} 行")
    else:
        print(f"检查完成，共发现 {total_issues} 个问题行")
    print("=" * 80)

if __name__ == "__main__":
    # 文件列表
    files = [
        r"E:\kSource\blog\invisible\study_notes\k00_english_basics.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_exam.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit1.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit1_en.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit1_zh.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit2.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit2_en.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit2_zh.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit4a.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit4a_en.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit4a_zh.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit4b.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit4b_en.md",
        r"E:\kSource\blog\invisible\study_notes\k01_graduate_english_unit4b_zh.md",
    ]

    main(files)
