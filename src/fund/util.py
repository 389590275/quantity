# -*- coding：utf-8
# @Time   :2024/7/18 15:06
# @Author :ghostgril
# @Email  :1690085531@qq.com
# @File   :util.py
import os
from datetime import datetime


def read_file_by_line(file_path):
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                lines.append(str.strip(line))
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


def clear_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def append_line_to_file(file_path, line):
    """向文件追加一行内容"""
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(line + '\n')
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_now_date():
    date = datetime.now().strftime("%Y-%m-%d %H:%m")
    return date


if __name__ == "__main__":
    # append_line_to_file("./ret.txt", "111")
    print(get_now_date())