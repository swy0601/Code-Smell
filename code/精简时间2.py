import os
import pandas as pd

# 定义函数，处理单个CSV文件
def process_csv_file(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path, encoding='latin1')
    
    # 处理时间数据
    time_data = df.iloc[0, 1]
    modified_time = process_time(time_data)
    df.iloc[0, 1] = modified_time
    
    # 保存修改后的文件
    df.to_csv(file_path, index=False)

# 定义函数，处理时间数据格式
def process_time(time_data):
    # 去除英文字符并替换“-”为“.”
    modified_time = ''.join(char if char.isdigit() or char == '.' else '' for char in time_data)
    modified_time = modified_time.replace('-', '.')
    return modified_time

# 处理文件夹中的所有CSV文件
def process_csv_folder(folder_path):
    # 处理文件夹中的所有文件
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file_path.endswith('.csv'):
            process_csv_file(file_path)

# 调用函数处理文件夹中的所有CSV文件
folder_path = 'C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据\\pmd'  # 替换为你的文件夹路径
process_csv_folder(folder_path)
