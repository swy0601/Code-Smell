import os
import csv

def calculate_sum_and_write_to_csv(input_folder_path, output_csv_path):
    # 打开输出CSV文件
    with open(output_csv_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['Version', 'Sum of 8th Column'])  # 写入表头

        # 遍历文件夹
        for folder_name in os.listdir(input_folder_path):
            folder_path = os.path.join(input_folder_path, folder_name)
            # 检查是否为文件夹
            if os.path.isdir(folder_path):
                # 构造typeMetrics.csv文件路径
                csv_file_path = os.path.join(folder_path, 'typeMetrics.csv')
                if os.path.exists(csv_file_path):
                    # 读取typeMetrics.csv文件并计算第八列从第二行到最后一行的总和
                    with open(csv_file_path, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        rows = list(csv_reader)
                        version = folder_name  # 版本号即文件夹名字
                        sum_of_eighth_column = sum(float(row[7]) for row in rows[1:])  # 第八列从第二行到最后一行的总和
                        # 写入结果到输出CSV文件
                        csv_writer.writerow([version, sum_of_eighth_column])
                        print(f"已处理文件夹 {folder_name}，总和为 {sum_of_eighth_column}")

# 输入文件夹路径
input_folder_path = r"C:\Users\指锁星河\Desktop\Final\analyse\JAVA_all\robolectric_done"
# 输出CSV文件路径
output_csv_path = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\robolectric.csv"

# 执行函数
calculate_sum_and_write_to_csv(input_folder_path, output_csv_path)
