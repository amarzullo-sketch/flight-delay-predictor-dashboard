import pandas as pd

df = pd.read_csv(r"C:\Users\aless\OneDrive\Desktop\Flight delayed project\Combined data\combined_flights_q1_2024.csv")

sample_df = df.head(1000)

sample_df.to_csv(r"C:\Users\aless\OneDrive\Desktop\Flight delayed project\Sample\sample_flights_q1_2024.csv", index=False)

print(sample_df.shape)
print(sample_df.head())