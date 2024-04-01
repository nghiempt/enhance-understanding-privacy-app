import pandas as pd

# Read data from CSV file
file_path = ''
df = pd.read_csv(file_path)

# Switch 'incomplete' and 'incorrect' columns
df['incomplete'], df['incorrect'] = df['incorrect'], df['incomplete']

# Write updated data back to the file
df.to_csv(file_path, index=False)

print("Columns switched and data written back to the file.")
