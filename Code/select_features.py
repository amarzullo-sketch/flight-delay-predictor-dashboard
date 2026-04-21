from pathlib import Path
import pandas as pd

base_path = Path(__file__).resolve().parent.parent

input_path = base_path / "Cleaned Data" / "clean_flights.csv"
output_path = base_path / "Cleaned Data" / "selected_flights.csv"

df = pd.read_csv(input_path)

feature_cols = [
    "DEP_DELAY",
    "TAXI_OUT",
    "AIR_TIME",
    "DISTANCE",
    "MONTH",
    "OP_UNIQUE_CARRIER",
    "is_delayed"
]

df = df[[col for col in feature_cols if col in df.columns]].copy()

df = df.dropna()

print(df.head())
print(df.info())
print("Final row count:", len(df))

df.to_csv(output_path, index=False)