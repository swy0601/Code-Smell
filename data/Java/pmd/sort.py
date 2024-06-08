import pandas as pd
import matplotlib.pyplot as plt

# 定义文件列表
file_list = [ "PMD\\时间对比\\18.3.csv", "PMD\\时间对比\\18.6.csv", "PMD\\时间对比\\18.9.csv", "PMD\\时间对比\\18.12.csv", "PMD\\时间对比\\19.3.csv", "PMD\\时间对比\\19.6.csv", "PMD\\时间对比\\19.9.csv", "PMD\\时间对比\\19.12.csv", "PMD\\时间对比\\20.3.csv", "PMD\\时间对比\\20.6.csv", "PMD\\时间对比\\20.9.csv", "PMD\\时间对比\\20.12.csv", "PMD\\时间对比\\21.3.csv", "PMD\\时间对比\\21.6.csv", "PMD\\时间对比\\21.9.csv", "PMD\\时间对比\\21.12.csv", "PMD\\时间对比\\22.3.csv", "PMD\\时间对比\\22.6.csv", "PMD\\时间对比\\22.9.csv", "PMD\\时间对比\\22.12.csv", "PMD\\时间对比\\23.3.csv", "PMD\\时间对比\\23.6.csv", "PMD\\时间对比\\23.9.csv", "PMD\\时间对比\\23.12.csv"]

# 初始化一个空的DataFrame
magic_df = pd.DataFrame(columns=['File', 'Magic Number'])

# 遍历文件列表
for file in file_list:
    # 读取CSV文件，指定编码为GB2312
    df = pd.read_csv(file, encoding='GB2312')

    # 找到Magic Number所在的单元格位置
    magic_column = df.columns[df.isin(['Magic Number']).any()][0]
    magic_row = df[df.eq('Magic Number').any(axis=1)].index[0]

    # 获取Magic Number右侧单元格的数值
    magic_number = df.iloc[magic_row, df.columns.get_loc(magic_column) + 1]

    # 将结果添加到DataFrame中
    magic_df = magic_df.append({'File': file, 'Magic Number': magic_number}, ignore_index=True)

# 绘制折线图
plt.plot(magic_df['File'], magic_df['Magic Number'], marker='o')
plt.xlabel('File')
plt.ylabel('Magic Number')
plt.title('Magic number变化过程')
plt.xticks(rotation=45, ha='right')  # 旋转X轴标签，使其更清晰
plt.tight_layout()

# 显示图形
plt.show()
