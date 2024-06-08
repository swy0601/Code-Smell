import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体，使用微软雅黑
plt.rcParams['font.family'] = 'Microsoft YaHei'
# 设置全局字体大小
plt.rcParams['font.size'] = 18  # 设置全局字体大小
plt.rcParams['axes.titlesize'] = 18  # 设置标题字体大小
plt.rcParams['axes.labelsize'] = 18  # 设置坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = 18  # 设置x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 18  # 设置y轴刻度字体大小
plt.rcParams['legend.fontsize'] = 16  # 设置图例字体大小

# Function to process each Excel file to extract the relevant data and calculate percentages
def process_excel_data(file_path):
    data = pd.read_excel(file_path)
    second_row = data.iloc[1]
    smells = {
        "names": [
            second_row["第一多"],
            second_row["第二多"],
            second_row["第三多"],
            second_row["第四多"],
            second_row["第五多"]
        ],
        "counts": [
            second_row["数量"],
            second_row["数量.1"],
            second_row["数量.2"],
            second_row["数量.3"],
            second_row["数量.4"]
        ],
    }
    return smells

# File paths for all uploaded Excel files
file_paths = [
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\certbot.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\locust.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\rasa.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\keras.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\ludwig.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\mindsdb.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\fastapi.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\scrapy.xlsx",
    "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333\\youtube.xlsx"
]

# Process each file and store the results
smells_data = {os.path.splitext(os.path.basename(file_path))[0]: process_excel_data(file_path) for file_path in file_paths}

# Set up the figure and axis for the horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(14, 10))
positions = range(len(smells_data))

# Assign specific colors to each unique smell type across all files
unique_smells = set(smell for data in smells_data.values() for smell in data['names'])
color_map = {smell: plt.cm.tab20(i/len(unique_smells)) for i, smell in enumerate(unique_smells)}

# Add bars for each smell type dynamically according to the actual data
for idx, (name, data) in enumerate(smells_data.items()):
    sorted_data = sorted(zip(data['names'], data['counts']), key=lambda x: x[1], reverse=True)[:5]
    total_count = sum(count for _, count in sorted_data)
    left = 0  # Start position for the first smell in each bar
    for smell, count in sorted_data:
        percentage = count / total_count * 100
        ax.barh(idx, count, left=left, color=color_map[smell], label=smell if smell not in ax.get_legend_handles_labels()[1] else "")
        left += count

# Setting labels, titles, and a complete legend
ax.set_xlabel('Count of Code Smells')
ax.set_ylabel('Projects')  # 添加纵轴标题
ax.set_yticks(positions)
ax.set_yticklabels(smells_data.keys())
handles, labels = ax.get_legend_handles_labels()

# 将图例放置在图片内部右下角，并设置透明度
ax.legend(handles, labels, title='Type of Code Smells', loc='lower right', framealpha=0.5)

plt.tight_layout()
plt.show()
