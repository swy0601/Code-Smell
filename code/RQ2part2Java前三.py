import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题
# 设置全局字体大小
plt.rcParams['font.size'] = 16  # 设置全局字体大小
plt.rcParams['axes.titlesize'] = 16  # 设置标题字体大小
plt.rcParams['axes.labelsize'] = 16  # 设置坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = 16  # 设置x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 16  # 设置y轴刻度字体大小
plt.rcParams['legend.fontsize'] = 16  # 设置图例字体大小

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
    colors = ['b', 'g', 'r']
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
            if smell in ['Magic Number', 'Long Statement', 'Unutilized Abstraction']:
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
    
    plt.xlabel('Time')
    plt.ylabel('Number of Code Smells')
    # plt.title('Java中出现前三的代码坏味演化')
    
    # 调整图例位置并放置在图像绘制区域外上方
    plt.legend(bbox_to_anchor=(0.5, 1.15), loc='upper center', ncol=3)
    
    plt.grid(True)
    plt.show()


# 调用函数进行处理
folder_path = 'C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据'  # 替换为你的文件夹路径
dataframes = read_csv_files(folder_path)
plot_line_chart(dataframes)
