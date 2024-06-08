import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def correct_month(month):
    # Ensure the month is within the correct range
    if month > 12:
        month = round(month / 10)
    return month

def process_excel_folder(folder_path):
    project_data = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            try:
                df = pd.read_excel(file_path, engine='openpyxl', header=None)
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
                continue
            
            for index, row in df.iloc[1:].iterrows():
                year_month = row[0]
                if pd.isnull(year_month):
                    continue
                # Split year and month, handling decimals
                year, month = divmod(year_month * 100, 100)
                year, month = int(year), int(month)
                month = correct_month(month)  # Correct the month value if needed
                time_node = datetime(year=int(2000 + year), month=month, day=1)
                
                dividend = row[1]
                divisor_columns = [15, 17, 19, 21, 23]
                divisor = sum(row[col] for col in divisor_columns if not pd.isnull(row[col]))
                
                result = divisor / dividend if dividend else 0
                project_data.setdefault(time_node, []).append(result)
    
    for time_node, values in project_data.items():
        project_data[time_node] = sum(values) / len(values) if values else 0
    return project_data

def plot_line_chart(project_data):
    sorted_data = sorted(project_data.items(), key=lambda x: x[0])
    x = [item[0] for item in sorted_data]
    y = [item[1] for item in sorted_data]
    plt.plot(x, y, marker='o')
    plt.xlabel('时间')
    plt.ylabel('积聚程度')
    plt.title('Python项目中积聚程度的时间演化')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    excel_folder_path = 'C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\python处理数据\\333'
    project_data = process_excel_folder(excel_folder_path)
    plot_line_chart(project_data)
