import csv
import os
import jieba

# 定义CSV文件夹路径
csv_folder = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JAVA_all\\robolectric合并"

# 定义输出CSV文件夹路径
output_folder = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据\\robolectric"

# 获取CSV文件夹下的所有文件名
csv_files = os.listdir(csv_folder)

# 遍历每个CSV文件
for csv_file_name in csv_files:
    # 构建完整的CSV文件路径
    csv_file_path = os.path.join(csv_folder, csv_file_name)

    # 读取CSV文件
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

    # 构建输出CSV文件路径
    output_csv_path = os.path.join(output_folder, f"{csv_file_name[:-4]}_词频统计.csv")

    # 打开表格文件，若表格文件不存在则创建
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['列名', '词', '出现次数'])  # 写表格表头

        # 遍历每一列的词频统计结果
        for col_name, counts in column_counts.items():
            items = list(counts.items())
            items.sort(key=lambda x: x[1], reverse=True)

            # 将前5个出现次数最多的词写入表格
            for i in range(min(5, len(items))):
                writer.writerow([col_name, items[i][0], items[i][1]])
