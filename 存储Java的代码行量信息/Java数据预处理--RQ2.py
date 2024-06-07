import pandas as pd
import os

def extract_data(input_folder, output_file):
    csv_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.csv')]
    print(f"Found {len(csv_files)} CSV files.")

    new_data = pd.DataFrame()

    for file in csv_files:
        print(f"Processing file: {file}")  # Displaying the file being processed
        try:
            # Attempt to read CSV with GBK encoding
            data = pd.read_csv(file, header=None, encoding='GBK')
            new_entry = pd.DataFrame({
                '新增第三列数据': [data.iloc[1, 1] if data.shape[1] > 1 else None],
                '新增第四列数据': [data.iloc[1, 2] if data.shape[1] > 2 else None]
            })
            new_data = pd.concat([new_data, new_entry], ignore_index=True)
        except Exception as e:
            print(f"Error processing file {file}: {e}")  # Display error message if any

    # Read existing output file, if it exists
    if os.path.exists(output_file):
        output_data = pd.read_csv(output_file)
        if output_data.shape[1] < 2:
            # Adding necessary empty columns if fewer than two exist
            while output_data.shape[1] < 2:
                output_data[f'Col_{output_data.shape[1]+1}'] = None
    else:
        print("Output file does not exist. Creating a new one with empty columns.")
        output_data = pd.DataFrame(columns=['第一列', '第二列'])

    output_data = pd.concat([output_data, new_data], axis=1)

    try:
        output_data.to_csv(output_file, index=False, encoding='utf_8_sig')
        print(f"Data successfully written to {output_file}")
    except Exception as e:
        print(f"Failed to write data to {output_file}: {e}")

input_folder = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\Java处理数据\\Mindustry"
output_file = "C:\\Users\\指锁星河\\Desktop\\Final\\analyse\\存储Java的代码行量信息\\Mindustry.csv"

extract_data(input_folder, output_file)
