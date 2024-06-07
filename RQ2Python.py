import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# 设置matplotlib配置以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题
# 设置全局字体大小
plt.rcParams['font.size'] = 16  # 设置全局字体大小
plt.rcParams['axes.titlesize'] = 16  # 设置标题字体大小
plt.rcParams['axes.labelsize'] = 16  # 设置坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = 16  # 设置x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 16  # 设置y轴刻度字体大小
plt.rcParams['legend.fontsize'] = 16  # 设置图例字体大小
def load_and_prepare_data(file_path):
    data = pd.read_excel(file_path)
    # 将 "时间/版本" 列重命名为 "Time"
    data.rename(columns={"时间/版本": "Time"}, inplace=True)
    # 确保Time列为字符串格式，并处理可能的非字符串输入
    data['Time'] = data['Time'].apply(lambda x: str(x).strip())
    # 将Time转换为日期对象，这里假设格式总是 'yy.mm'
    data['Time'] = data['Time'].apply(lambda x: datetime.strptime(x, "%y.%m") if "." in x else x)
    data.sort_values('Time', inplace=True)
    # 转换回字符串格式，用于标签显示
    data['Time'] = data['Time'].dt.strftime('%y.%m')
    return data[['Time', '代码坏味总数', '代码LOC']]

def combine_and_plot_data(files):
    all_data = [load_and_prepare_data(file) for file in files]
    combined_data = pd.DataFrame()
    
    for data in all_data:
        combined_data = pd.concat([combined_data, data])
    combined_data = combined_data.groupby('Time').sum().reset_index()
    combined_data['坏味率'] = combined_data['代码坏味总数'] / combined_data['代码LOC']
    
    fig, ax1 = plt.subplots(figsize=(16, 8))
    color = 'tab:blue'
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Code Smell Rate', color=color)
    ax1.bar(combined_data['Time'], combined_data['坏味率'], color=color, alpha=0.6, label='Code Smell Rate')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_xticks(combined_data['Time'].index)
    ax1.set_xticklabels(combined_data['Time'], rotation=90)

    # 调整坏味率的y轴范围
    ax1.set_ylim([0, combined_data['坏味率'].max() * 1.1])  # 假设最大值的110%为上界

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('LOC', color=color)
    ax2.plot(combined_data['Time'], combined_data['代码LOC'], color=color, marker='o', linestyle='-', label='代码LOC')
    ax2.tick_params(axis='y', labelcolor=color)

    # plt.title('Python总体代码坏味率与行数趋势')
    fig.tight_layout()
    plt.show()

# List of file paths
files = [
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\certbot.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\youtube.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\fastapi.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\keras.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\ludwig.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\mindsdb.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\locust.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\scrapy.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\rasa.xlsx"
]

combine_and_plot_data(files)
