import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 递归读取文件夹中的所有CSV文件
def read_csv_files(folder_path):
    dataframes = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path, encoding='latin1')
                dataframes.append(df)
    return dataframes

# 解析时间字符串为日期对象
def parse_time(time_str):
    return datetime.strptime(time_str, '%y.%m')

# 绘制折线图
def plot_line_chart(dataframes):
    all_data = {}  # 存储所有数据
    
    # 定义一组颜色，可以根据需要自行调整颜色
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray']
    color_index = 0
    
    for df in dataframes:
        # 尝试解析时间信息
        try:
            time = parse_time(df.iloc[0, 1])
        except ValueError:
            continue  # 如果日期格式不正确，则跳过此文件
        
        # 获取代码坏味信息和数量
        smells = df.iloc[11:16, 1].tolist()
        smell_counts = df.iloc[11:16, 2].tolist()
        for smell, count in zip(smells, smell_counts):
            if (time, smell) not in all_data:
                all_data[(time, smell)] = 0
            all_data[(time, smell)] += int(count)
    
    # 整理数据用于绘图
    plot_data = {}
    for (time, smell), count in all_data.items():
        if smell not in plot_data:
            plot_data[smell] = []
        plot_data[smell].append((time, count))

    # 对数据进行排序
    for smell in plot_data:
        plot_data[smell].sort(key=lambda x: x[0])
    
    # 绘制折线图
    plt.figure(figsize=(10, 6))
    for smell, values in plot_data.items():
        times = [x[0] for x in values]
        counts = [x[1] for x in values]
        plt.plot(times, counts, marker='o', label=smell, color=colors[color_index])
        color_index = (color_index + 1) % len(colors)  # 循环使用颜色列表中的颜色
    
    plt.xlabel('时间')
    plt.ylabel('数量')
    plt.title('Java中出现前五的代码坏味演化')
    plt.legend()
    plt.grid(True)
    plt.show()


# 调用函数进行处理
folder_path = 'C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据'  # 替换为你的文件夹路径
dataframes = read_csv_files(folder_path)
plot_line_chart(dataframes)
