import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 设置中文字体，使用微软雅黑
plt.rcParams['font.family'] = 'Microsoft YaHei'

# 设置全局字体大小
plt.rcParams['font.size'] = 25  # 设置全局字体大小
plt.rcParams['axes.titlesize'] = 25  # 设置标题字体大小
plt.rcParams['axes.labelsize'] = 25  # 设置坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = 25  # 设置x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 25  # 设置y轴刻度字体大小
plt.rcParams['legend.fontsize'] = 25  # 设置图例字体大小

def plot_java_data(ax):
    def compile_code_smells(file_paths):
        code_smells_compilation = {}
        for file_path in file_paths:
            project_name = file_path.split('\\')[-1].split('.')[0]
            df = pd.read_csv(file_path, header=None, encoding='ISO-8859-1')
            smells_rows = df[df[0] == 'Code Smell'].iloc[:5, 1:3]
            code_smells_compilation[project_name] = {
                'smells': smells_rows[1].tolist(),
                'counts': [int(float(count)) for count in smells_rows[2].tolist()]
            }
        return code_smells_compilation

    file_paths = [
        # 请确保这些路径是正确的
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\baritone.csv",
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\GmsCore.csv",
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\graphhopper.csv",
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\karate.csv",
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\Mindustry.csv",
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\mybatis.csv",
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\pmd.csv",
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\pulsar.csv",
        "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\JavaRQ1\\robolectric.csv"
    ]

    compiled_smells = compile_code_smells(file_paths)
    unique_smells = set(smell for smells in compiled_smells.values() for smell in smells['smells'])
    smell_color_map = {smell: plt.cm.tab20(i / len(unique_smells)) for i, smell in enumerate(unique_smells)}

    handles = []
    for project, data in compiled_smells.items():
        bottom = 0
        for smell, count in zip(data['smells'], data['counts']):
            bar = ax.barh(project, count, left=bottom, color=smell_color_map[smell])
            bottom += count
            if smell not in [h.get_label() for h in handles]:
                handles.append(mpatches.Patch(color=bar.patches[0].get_facecolor(), label=smell))

    # 设置纵轴标题为 "Projects"
    ax.set_ylabel('Projects')
    ax.set_xlabel('Count of Code Smells')
    ax.legend(handles=handles, title='Type of Code Smells', loc='lower right', framealpha=0.5, fontsize=12)

# 创建一个子图的图形
fig, ax2 = plt.subplots(figsize=(10, 10))

plot_java_data(ax2)  # 绘制Java数据

plt.tight_layout()
plt.show()
