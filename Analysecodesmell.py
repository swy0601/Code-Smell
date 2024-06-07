import csv
import jieba
# 读取CSV文件
csv_file_path = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\PMD\\合并\\23.12.csv"
with open(csv_file_path, 'rt', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    # 获取列标题（表头）
    headers = next(csv_reader)

    # 创建一个字典用于存储每一列的词频统计
    column_counts = {header: {} for header in headers}

    # 遍历每一行数据
    for row in csv_reader:
        for col_index, cell in enumerate(row):
            # 将整个单元格作为一个词进行统计
            word = cell.strip()  # 如果需要去除首尾空格，可以使用 strip() 方法

            # 统计词频
            counts = column_counts[headers[col_index]]
            if len(word) > 0:  # 确保单词不为空
                counts[word] = counts.get(word, 0) + 1

# 打开表格文件，若表格文件不存在则创建
output_csv_path = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\PMD\\时间对比\\23.12.csv"
with open(output_csv_path, 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(['列名', '词', '出现次数'])  # 写表格表头

    # 遍历每一列的词频统计结果
    for col_name, counts in column_counts.items():
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)

        # 将前5个出现次数最多的词写入表格
        for i in range(min(5, len(items))):
            writer.writerow([col_name, items[i][0], items[i][1]])
