import os
import re
import pandas as pd
from collections import defaultdict

def process_data_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    title_pattern = r'Title: (.*)'
    dialogue_pattern = r'Dialogue: [^,]*,(\d+:\d+:\d+)\.\d+,[^,]*'

    title = None
    timestamps = defaultdict(int)

    for line in content:
        if not title:
            title_match = re.match(title_pattern, line)
            if title_match:
                title = title_match.group(1)
                continue

        dialogue_match = re.match(dialogue_pattern, line)

        if dialogue_match:
            timestamp = dialogue_match.group(1)
            timestamps[timestamp] += 1

    top_timestamps = sorted(timestamps.items(), key=lambda x: x[1], reverse=True)[:3]

    return title, [x[0] for x in top_timestamps]


def main(input_folder, output_file):
    data = []

    for file in os.listdir(input_folder):
        if file.endswith('.txt'):
            file_path = os.path.join(input_folder, file)
            title, timestamps = process_data_file(file_path)
            data.append([title, timestamps[0], timestamps[1], timestamps[2]])

    df = pd.DataFrame(data, columns=['视频名称', '最高峰时间戳', '次高峰时间戳', '第三高峰时间戳'])
    df.to_excel(output_file, index=False)


if __name__ == '__main__':
    input_folder = '在这里填入弹幕文件所在文件夹'
    output_file = '输出数据表.xlsx'
    main(input_folder, output_file)