import pandas as pd
import matplotlib.pyplot as plt
import os

# 定义文件列表
file_list = [
    "PMD\\时间对比\\18.3.csv", "PMD\\时间对比\\18.6.csv", "PMD\\时间对比\\18.9.csv", "PMD\\时间对比\\18.12.csv",
    "PMD\\时间对比\\19.3.csv", "PMD\\时间对比\\19.6.csv", "PMD\\时间对比\\19.9.csv", "PMD\\时间对比\\19.12.csv",
    "PMD\\时间对比\\20.3.csv", "PMD\\时间对比\\20.6.csv", "PMD\\时间对比\\20.9.csv", "PMD\\时间对比\\20.12.csv",
    "PMD\\时间对比\\21.3.csv", "PMD\\时间对比\\21.6.csv", "PMD\\时间对比\\21.9.csv", "PMD\\时间对比\\21.12.csv",
    "PMD\\时间对比\\22.3.csv", "PMD\\时间对比\\22.6.csv", "PMD\\时间对比\\22.9.csv", "PMD\\时间对比\\22.12.csv",
    "PMD\\时间对比\\23.3.csv", "PMD\\时间对比\\23.6.csv", "PMD\\时间对比\\23.9.csv", "PMD\\时间对比\\23.12.csv"
]

# 关键词列表
keywords = ['Magic Number', 'Long Statement', 'Unnecessary Abstraction', 'Unutilized Abstraction','Broken Hierarchy','Complex Conditional','Cyclic-Dependent Modularization']

# 初始化一个空的DataFrame用于存放所有关键词的结果
results_df = pd.DataFrame()

# 遍历每个关键词
for keyword in keywords:
    # 初始化一个空的DataFrame用于当前关键词
    df_keyword = pd.DataFrame(columns=['File', keyword])

    # 遍历文件列表
    for file in file_list:
        df = pd.read_csv(file, encoding='GB2312')
        file_name = os.path.basename(file) 

        # 检查是否找到了关键词
        if df.isin([keyword]).any().any():
            # 找到关键词所在的单元格位置
            keyword_column = df.columns[df.isin([keyword]).any()][0]
            keyword_row = df[df.eq(keyword).any(axis=1)].index[0]

            # 获取关键词右侧单元格的数值
            keyword_value = df.iloc[keyword_row, df.columns.get_loc(keyword_column) + 1]
        else:
            # 如果没有找到关键词，设置一个默认值0
            keyword_value = 0

        # 将结果添加到DataFrame中
        df_keyword = df_keyword.append({'File': file_name, keyword: keyword_value}, ignore_index=True)

    # 合并当前关键词的结果到最终的DataFrame中
    if results_df.empty:
        results_df = df_keyword
    else:
        results_df = pd.merge(results_df, df_keyword, on='File')

# 绘制折线图，为每个关键词设置不同的颜色和标记
for keyword in keywords:
    plt.plot(results_df['File'], results_df[keyword], marker='o', label=keyword)

plt.xlabel('File')
plt.ylabel('Value')
plt.title('CodeSmell Variation Over Time')
plt.xticks(rotation=45, ha='right')  # 旋转X轴标签，使其更清晰
plt.tight_layout()
plt.legend()  # 添加图例

# 显示图形
plt.show()
