import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def process_project_folder(folder_path):
    project_data = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
            except UnicodeDecodeError:
                # 如果utf-8解码失败，则尝试使用gbk编码
                df = pd.read_csv(file_path, encoding='gbk')
            # 获取时间节点信息并转换为时间戳格式
            time_node_str = df.iloc[0, 1]
            # 在时间节点信息后面加上一个虚拟的日期（例如01号），以便使用datetime解析
            time_node_str = '01.' + time_node_str
            time_node = datetime.strptime(time_node_str, '%d.%y.%m')
            # 获取第三列第一行数据作为被除数
            dividend = df.iloc[0, 2]
            # 获取第三列第二行到第六行的数据进行相加作为除数
            divisor = df.iloc[1:6, 2].sum()
            # 计算结果
            result = divisor / dividend
            project_data[time_node] = result
    return project_data

def process_top_folder(top_folder_path):
    all_project_data = {}
    for project_folder_name in os.listdir(top_folder_path):
        project_folder_path = os.path.join(top_folder_path, project_folder_name)
        if os.path.isdir(project_folder_path):
            project_data = process_project_folder(project_folder_path)
            all_project_data[project_folder_name] = project_data
    return all_project_data

def plot_line_chart(project_data):
    for project_name, data in project_data.items():
        # 对时间节点进行排序
        sorted_data = sorted(data.items(), key=lambda x: x[0])
        x = [item[0] for item in sorted_data]
        y = [item[1] for item in sorted_data]
        plt.plot(x, y, label=project_name)

    plt.xlabel('Time Node')
    plt.ylabel('Value')
    plt.title('Evolution of Values Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    top_folder_path = 'C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据'
    all_project_data = process_top_folder(top_folder_path)
    plot_line_chart(all_project_data)
