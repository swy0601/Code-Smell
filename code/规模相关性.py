import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 构建数据
data_java = {
    "Repository": ["pmd", "pulsar", "robolectric", "graphhopper", "GmsCore", "Mindustry", "karate", "mybatis-plus", "baritone"],
    "LOC": [131676, 485479, 222765, 98499, 56954, 93925, 40128, 41112, 23970],
    "Bad Smell Count": [8509, 54311, 21092, 31701, 3549, 14381, 1654, 2542, 2130],
    "坏味率 (%)": [6.46, 11.19, 9.47, 32.18, 6.23, 15.31, 4.12, 6.18, 8.89]
}

data_python = {
    "Repository": ["rasa", "keras", "youtube-dl", "fastapi", "ludwig", "mindsdb", "certbot", "scrapy", "locust"],
    "LOC": [120176, 136082, 140075, 94593, 96373, 91078, 45868, 49575, 23630],
    "Bad Smell Count": [621, 920, 1136, 1577, 1143, 1763, 601, 841, 457],
    "坏味率 (%)": [3.63, 0.68, 0.81, 1.67, 1.19, 1.94, 1.31, 1.70, 1.93]
}

df_java = pd.DataFrame(data_java)
df_python = pd.DataFrame(data_python)

# 定义兼容的填充型标记
markers = ["o", "s", "^", "P", "*", "X", "D", "d", "h"]

# 绘制散点图
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(data=df_java, x="LOC", y="坏味率 (%)", hue="Repository", style="Repository", markers=markers, s=100)
plt.title("Java项目")
plt.grid(True)

plt.subplot(1, 2, 2)
sns.scatterplot(data=df_python, x="LOC", y="坏味率 (%)", hue="Repository", style="Repository", markers=markers, s=100)
plt.title("Python项目")
plt.grid(True)

plt.tight_layout()
plt.show()

# 计算相关性系数
corr_coef_java, _ = pearsonr(df_java["LOC"], df_java["坏味率 (%)"])
corr_coef_python, _ = pearsonr(df_python["LOC"], df_python["坏味率 (%)"])

print(f"Java Projects Correlation Coefficient: {corr_coef_java}")
print(f"Python Projects Correlation Coefficient: {corr_coef_python}")
