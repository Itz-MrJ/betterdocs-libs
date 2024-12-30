import pandas as pd

# Data to write to the file
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "Salary": [55000, 48000, 62000],
}

# Create a DataFrame
df_to_write = pd.DataFrame(data)

# Filepath for the tab-separated file
file_path = "data.csv"

# Writing the DataFrame to a tab-separated file
df_to_write.to_csv(file_path, sep="\t", index=False)

# Reading the file back into a DataFrame
df_read = pd.read_csv(filepath_or_buffer=file_path, delimiter="\t", header=0, index_col='ID')

# Display the DataFrame read from the file
print(df_read)
'''
Output:
       Name  Age  Salary
ID                      
1     Alice   30   55000
2       Bob   25   48000
3   Charlie   35   62000
'''