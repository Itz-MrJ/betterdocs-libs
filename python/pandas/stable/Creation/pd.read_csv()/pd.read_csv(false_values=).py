import pandas as pd

# Data to write to the file
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 20, 10],
    "Salary": [55000, 48000, 62000],
    "IsActive": ["no", "maybe", "yes"]
}

# Create a DataFrame
df_to_write = pd.DataFrame(data)

# Filepath for the tab-separated file
file_path = "data.csv"

# Writing the DataFrame to a tab-separated file
df_to_write.to_csv(file_path, sep="\t", index=False)

# Reading the file back into a DataFrame using true_values
df_read = pd.read_csv(filepath_or_buffer=file_path, sep="\t", header=0, true_values=["yes"], false_values=["no", "maybe"])

# Display the DataFrame read from the file
print(df_read)
'''
Output:
   ID     Name  Age  Salary  IsActive
0   1    Alice   30   55000     False
1   2      Bob   20   48000     False
2   3  Charlie   10   62000      True
'''