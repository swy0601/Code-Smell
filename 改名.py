import os

def rename_csv_files(folder_path):
    # 获取目录下所有文件
    files = os.listdir(folder_path)
    
    for file_name in files:
        # 检查文件是否为CSV格式
        if file_name.endswith('.csv'):
            # 构造新的文件名
            new_name = file_name.replace('.csv', '_词频统计.csv')
            # 构造文件的完整路径
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            # 执行重命名操作
            os.rename(old_path, new_path)
            print(f"已将文件 {file_name} 重命名为 {new_name}")

# 指定目标文件夹路径
folder_path = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据\\pmd"
# 调用函数进行重命名操作
rename_csv_files(folder_path)
