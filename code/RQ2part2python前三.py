import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 设置全局字体大小
plt.rcParams['font.size'] = 16  # 设置全局字体大小
plt.rcParams['axes.titlesize'] = 16  # 设置标题字体大小
plt.rcParams['axes.labelsize'] = 16  # 设置坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = 16  # 设置x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 16  # 设置y轴刻度字体大小
plt.rcParams['legend.fontsize'] = 12  # 设置图例字体大小

# 递归读取文件夹中的所有Excel文件
def read_excel_files(folder_path):
    dataframes = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                df = pd.read_excel(file_path, engine='openpyxl')
                dataframes.append(df)
    return dataframes

# 解析时间字符串为日期对象
def parse_time(time_str):
    return datetime.strptime(str(time_str), '%y.%m')

# 绘制折线图
def plot_line_chart(dataframes):
    all_data = {}
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray']
    color_index = 0

    for df in dataframes:
        print("Processing dataframe:")
        print(df.head())  # 打印 dataframe 的前几行来检查数据

        for index, row in df.iterrows():
            try:
                time = parse_time(row.iloc[0])
            except ValueError:
                continue

            smells = row.iloc[3:13:2].tolist()
            smell_counts = row.iloc[4:14:2].tolist()
            
            for smell, count in zip(smells, smell_counts):
                if (time, smell) not in all_data:
                    all_data[(time, smell)] = 0
                all_data[(time, smell)] += int(count)

    # 整理数据用于绘图，并筛选每个时间点前三的坏味
    top_smells_per_time = {}
    for (time, smell), count in all_data.items():
        if time not in top_smells_per_time:
            top_smells_per_time[time] = []
        top_smells_per_time[time].append((smell, count))
        top_smells_per_time[time] = sorted(top_smells_per_time[time], key=lambda x: x[1], reverse=True)[:3]  # 只保留前三的坏味

    plot_data = {}
    for time, smells_info in top_smells_per_time.items():
        for smell, count in smells_info:
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
        color_index = (color_index + 1) % len(colors)

    plt.xlabel('Time')
    plt.ylabel('Number of Code Smells')
    # plt.title('Python中出现前三的代码坏味演化')
    plt.legend(bbox_to_anchor=(0.5, 1.15), loc='upper center', ncol=3)
    plt.grid(True)
    plt.show()

# 调用函数进行处理
folder_path = 'C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333'  # 替换为你的文件夹路径
dataframes = read_excel_files(folder_path)
plot_line_chart(dataframes)
