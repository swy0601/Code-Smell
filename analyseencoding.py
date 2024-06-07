import chardet
import pandas as pd

# 使用 chardet 检测文件编码
with open("C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据\\baritone\\2018.12_词频统计.csv", 'rb') as f:
    result = chardet.detect(f.read())
print(result)
# # 读取 CSV 文件时指定检测到的编码
# df_unknown = pd.read_csv("file_unknown_encoding.csv", encoding=result['encoding'])
