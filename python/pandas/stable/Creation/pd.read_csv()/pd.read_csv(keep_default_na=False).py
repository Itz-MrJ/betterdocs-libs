import pandas as pd

# Data to write to the file
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "null"],
    "Age": [30, "NA", 10],
    "Salary": [55000, 48000, 62000],
}

# Create a DataFrame
df_to_write = pd.DataFrame(data)

# Filepath for the tab-separated file
file_path = "data.csv"

# Writing the DataFrame to a tab-separated file
df_to_write.to_csv(file_path, sep="\t", index=False)

# Reading the file back into a DataFrame 
df_read = pd.read_csv(filepath_or_buffer=file_path, sep="\t", header=0, keep_default_na=False)

# Display the DataFrame read from the file
print(df_read)
'''
Output:
   ID   Name Age  Salary
0   1  Alice  30   55000
1   2    Bob  NA   48000
2   3   null  10   62000
'''