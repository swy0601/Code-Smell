import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
csv_file_path = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Mindustry\\时间对比\\23.12.csv"
df = pd.read_csv(csv_file_path, encoding='gb2312')

# 提取目标数据
target_data = df.iloc[1:6, 2]
print(target_data)
# 设置标签和颜色
labels =df.iloc[1:6, 1]
# labels =["logging.log4j", "log4j.core.layout", "log4j.core.appender", "log4j.core.filter", "log4j.core.appender.rolling"]
colors = ['yellow', 'blue', 'green', 'red', 'purple']

# 绘制饼状图
plt.pie(target_data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# 设置图的标题
plt.title("Scatter of Codesmell")

# 显示图
plt.show()
