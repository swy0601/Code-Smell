import os
import re

def rename_csv_files(folder_path):
    # 获取 karate 文件夹下所有文件
    files = os.listdir(folder_path)
    
    for file_name in files:
        # 检查文件是否为CSV格式并且包含日期部分
        if file_name.endswith('.csv') and re.search(r'\d+-\d+', file_name):
            old_file_path = os.path.join(folder_path, file_name)
            # 获取日期部分，例如 18-3
            match = re.search(r'(\d+)-(\d+)', file_name)
            if match:
                year, month = match.groups()
                # 构造新的文件名，例如 2018.3_词频统计.csv
                new_file_name = f"20{year}.{month}_词频统计.csv"
                new_file_path = os.path.join(folder_path, new_file_name)
                # 执行重命名操作
                os.rename(old_file_path, new_file_path)
                print(f"已将文件 {file_name} 重命名为 {new_file_name}")

# 指定 karate 文件夹路径
folder_path = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据\\pulsar"
# 调用函数进行重命名操作
rename_csv_files(folder_path)
