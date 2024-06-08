import pandas as pd
import os

# 定义数据文件夹路径
data_folder = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JAVA_all\\robolectric_done\\"

# 定义目标文件夹路径
output_folder = "C:\\Users\指锁星河\\Desktop\\Final\\analyse\\JAVA_all\\robolectric合并"

# 获取所有文件夹名称
folder_names = os.listdir(data_folder)

# 遍历文件夹
for folder_name in folder_names:
    # 构建完整的路径
    folder_path = os.path.join(data_folder, folder_name)
    
    # 读取两个 Excel 文件
    csv_file_path1 = os.path.join(folder_path, "designCodeSmells.csv")
    csv_file_path2 = os.path.join(folder_path, "implementationCodeSmells.csv")
    
    df1 = pd.read_csv(csv_file_path1)
    df2 = pd.read_csv(csv_file_path2)

    # 按照相同的四列进行合并
    merged_df = pd.merge(df1, df2, on=['Project Name', 'Package Name', 'Type Name', 'Code Smell'], how='outer')

    # 构建输出路径
    output_csv_path = os.path.join(output_folder, f"{folder_name}.csv")

    # 检查目录是否存在，如果不存在就创建
    output_directory = os.path.dirname(output_csv_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 保存合并后的数据到新的 CSV 文件
    merged_df.to_csv(output_csv_path, index=False)
