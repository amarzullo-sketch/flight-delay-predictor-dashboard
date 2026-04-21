import pandas as pd
import glob
import os

folder_path = r"C:\Users\aless\OneDrive\Desktop\Flight delayed project\raw data"

files = glob.glob(os.path.join(folder_path, "*", "*.csv"))

print(files)  # lets you check that it actually found the 3 csv files

df = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)

df.to_csv(os.path.join(folder_path, "combined_flights_q1_2024.csv"), index=False)

print(df.shape)
print(df.head())