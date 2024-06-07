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
    data = pd.read_csv(file_path, usecols=[0, 1, 3], header=None, skiprows=1, nrows=22)
    data.columns = ['Time', '代码LOC', '代码坏味总数']
    # 假设时间/版本格式是 'yy.mm'，确保所有时间格式正确并转换为日期对象
    data['Time'] = data['Time'].astype(str)
    data['Time'] = data['Time'].apply(lambda x: datetime.strptime(x, "%y.%m"))
    data.sort_values('Time', inplace=True)
    # 重新转换为字符串用于显示
    data['Time'] = data['Time'].dt.strftime('%y.%m')
    return data

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
    ax1.set_xticks(range(len(combined_data['Time'])))
    ax1.set_xticklabels(combined_data['Time'], rotation=90)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('LOC', color=color)
    ax2.plot(combined_data['Time'], combined_data['代码LOC'], color=color, marker='o', linestyle='-', label='LOC')
    ax2.tick_params(axis='y', labelcolor=color)

    # plt.title('Java总体代码坏味率与行数趋势')
    fig.tight_layout()
    plt.show()

# List of file paths
files = [
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\Mindustry.csv",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\baritone.csv",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\GmsCore.csv",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\graphhopper.csv",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\pmd.csv",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\karate.csv",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\mybatis.csv",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\pulsar.csv",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\robolectric.csv"
]

combine_and_plot_data(files)
