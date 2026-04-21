from pathlib import Path
import pandas as pd

base_path = Path(__file__).resolve().parent.parent

input_path = base_path / "Cleaned Data" / "flights_with_target.csv"
output_path = base_path / "Cleaned Data" / "clean_flights.csv"

df = pd.read_csv(input_path)

numeric_cols = ["ARR_DELAY", "DEP_DELAY", "AIR_TIME", "DISTANCE", "TAXI_OUT", "TAXI_IN"]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

needed_cols = ["ARR_DELAY", "DEP_DELAY", "AIR_TIME", "DISTANCE", "is_delayed"]
df = df.dropna(subset=[col for col in needed_cols if col in df.columns])

df = df.drop_duplicates()

print(df.info())
print(df.head())
print("Final row count:", len(df))

df.to_csv(output_path, index=False)