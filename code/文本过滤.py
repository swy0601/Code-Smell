# Define function to filter out specified keywords from a text file
def filter_keywords(input_file, output_file, keywords):
    with open(input_file, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()

    cleaned_lines = []
    for line in lines:
        if not any(keyword.lower() in line.lower() for keyword in keywords):
            cleaned_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as fout:
        fout.writelines(cleaned_lines)

# Define the keywords to remove
keywords_to_remove = ["pulsar", "mindustry", "com", "apache", "robolectric", "karate", "google", "graphhopper","baritone","pmd","lang"]

# Define input and output file paths
input_file = 'output.txt'
filtered_output_file = 'filtered_output.txt'

# Filter the keywords and write to output file
filter_keywords(input_file, filtered_output_file, keywords_to_remove)
