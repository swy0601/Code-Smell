import pandas as pd
import matplotlib.pyplot as plt
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

#读取多个 CSV 文件
csv_files = [ "PMD\\时间对比\\18.3.csv", "PMD\\时间对比\\18.6.csv", "PMD\\时间对比\\18.9.csv", "PMD\\时间对比\\18.12.csv", "PMD\\时间对比\\19.3.csv", "PMD\\时间对比\\19.6.csv", "PMD\\时间对比\\19.9.csv", "PMD\\时间对比\\19.12.csv", "PMD\\时间对比\\20.3.csv", "PMD\\时间对比\\20.6.csv", "PMD\\时间对比\\20.9.csv", "PMD\\时间对比\\20.12.csv", "PMD\\时间对比\\21.3.csv", "PMD\\时间对比\\21.6.csv", "PMD\\时间对比\\21.9.csv", "PMD\\时间对比\\21.12.csv", "PMD\\时间对比\\22.3.csv", "PMD\\时间对比\\22.6.csv", "PMD\\时间对比\\22.9.csv", "PMD\\时间对比\\22.12.csv", "PMD\\时间对比\\23.3.csv", "PMD\\时间对比\\23.6.csv", "PMD\\时间对比\\23.9.csv", "PMD\\时间对比\\23.12.csv"]
dataframes = []

for file in csv_files:
    df = pd.read_csv(file, encoding='gb2312')
    dataframes.append(df)

#提取目标数据
plt.figure(figsize=(10, 6))

#绘制每一条折线
lines = []
for i in range(len(dataframes) - 1):
    current_df = dataframes[i]
    next_df = dataframes[i + 1]

    current_version = current_df.iloc[0, 1]
    next_version = next_df.iloc[0, 1]

    current_data_12 = current_df.iloc[11, 2]  
    next_data_12 = next_df.iloc[11, 2]  

    current_data_13 = current_df.iloc[12, 2]  # 当前版本的第三列第十三行的数据
    next_data_13 = next_df.iloc[12, 2]  # 下一个版本的第三列第十三行的数据

    current_data_14 = current_df.iloc[13, 2]  # 当前版本的第三列第十四行的数据
    next_data_14 = next_df.iloc[13, 2]  # 下一个版本的第三列第十四行的数据

    current_data_15 = current_df.iloc[14, 2]  # 当前版本的第三列第十五行的数据
    next_data_15 = next_df.iloc[14, 2]  # 下一个版本的第三列第十五行的数据

    current_data_16 = current_df.iloc[15, 2]  # 当前版本的第三列第十五行的数据
    next_data_16 = next_df.iloc[15, 2]  # 下一个版本的第三列第十五行的数据    

    # 绘制折线并获取线对象
    line_12, = plt.plot([current_version, next_version], [current_data_12, next_data_12], marker='o', color='yellow')
    line_13, = plt.plot([current_version, next_version], [current_data_13, next_data_13], marker='o', color='blue')
    line_14, = plt.plot([current_version, next_version], [current_data_14, next_data_14], marker='o', color='green')
    line_15, = plt.plot([current_version, next_version], [current_data_15, next_data_15], marker='o', color='red')
    line_16, = plt.plot([current_version, next_version], [current_data_16, next_data_16], marker='o', color='purple')

    # 将线对象加入列表
    lines.extend([line_12, line_13, line_14, line_15, line_16])

# 显示图例
plt.legend(lines, ["Magic Number", "Long Statement", "Unutilized Abstraction", "Long Parameter List", "Deficient Encapsulation"])


plt.xticks(fontsize=6)  # 修改字号大小为8
# 设置图的横纵坐标标签和标题
plt.xlabel("Version")
plt.ylabel("Frequency")
plt.title("Codesmell Over Versions")

# 显示图
plt.show()
