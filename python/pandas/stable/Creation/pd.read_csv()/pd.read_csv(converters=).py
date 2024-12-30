import pandas as pd

# Data to write to the file
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 20, 10],
    "Salary": [55000, 48000, 62000],
}

# Create a DataFrame
df_to_write = pd.DataFrame(data)

# Filepath for the tab-separated file
file_path = "data.csv"

# Writing the DataFrame to a tab-separated file
df_to_write.to_csv(file_path, sep="\t", index=False)

def half_the_age(age):
    return int(age)/2

# Reading the file back into a DataFrame
df_read = pd.read_csv(filepath_or_buffer=file_path, sep="\t", header=0, converters={"Age": half_the_age})

# Display the DataFrame read from the file
print(df_read)
'''
Output:
   ID     Name   Age  Salary
0   1    Alice  15.0   55000
1   2      Bob  10.0   48000
2   3  Charlie   5.0   62000
'''