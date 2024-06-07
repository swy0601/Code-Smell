import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

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
    time_str = str(time_str)  # 将时间数据转换为字符串类型
    return datetime.strptime(time_str, '%y.%m')


# 绘制折线图
def plot_line_chart(dataframes):
    all_data = {}  # 存储所有数据
    
    # 定义一组颜色，可以根据需要自行调整颜色
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray']
    color_index = 0
    
    for df in dataframes:
        print("Processing dataframe:")
        print(df.head())  # 打印 dataframe 的前几行来检查数据是否正确加载
        
        for index, row in df.iterrows():
            # 尝试解析时间信息
            try:
                time = parse_time(row.iloc[0])
                print("Parsed time:", time)  # 打印解析后的时间信息
            except ValueError:
                continue  # 如果日期格式不正确，则跳过此行数据
            
            # 获取代码坏味信息和数量
            smells = row.iloc[3:13:2].tolist()  # 代码坏味名称
            smell_counts = row.iloc[4:14:2].tolist()  # 代码坏味出现次数
            print("Smells:", smells)  # 打印代码坏味名称列表
            print("Smell counts:", smell_counts)  # 打印代码坏味出现次数列表
            
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
    plt.title('Python中出现前五的代码坏味演化')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # 将图例放在右上角
    plt.grid(True)
    plt.show()


# 调用函数进行处理
folder_path = 'C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333'  # 替换为你的文件夹路径
dataframes = read_excel_files(folder_path)
plot_line_chart(dataframes)
