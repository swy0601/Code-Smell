import os
import pandas as pd

# 定义函数，处理单个CSV文件
def process_csv_file(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path, encoding='latin1')
    
    # 修改时间数据
    time_data = df.iloc[0, 1]
    modified_time = modify_time(time_data)
    df.iloc[0, 1] = modified_time
    
    # 保存修改后的文件
    df.to_csv(file_path, index=False)

# 定义函数，修改时间数据格式
def modify_time(time_data):
    year, month = map(int, time_data.split('.'))
    # 将年份转换为两位数
    year %= 100
    return f"{year}.{month}"

# 遍历文件夹中的所有CSV文件并处理
def process_csv_folder(folder_path):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        process_csv_file(file_path)

# 调用函数处理文件夹中的CSV文件
folder_path = 'C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据\\robolectric'  # 替换为你的文件夹路径
process_csv_folder(folder_path)
