from pathlib import Path
import pandas as pd

base_path = Path(__file__).resolve().parent
csv_path = base_path / "combined_flights.csv"

df = pd.read_csv(csv_path)

df = df[(df["CANCELLED"] == 0) & (df["DIVERTED"] == 0)].copy()
df = df[df["ARR_DELAY"].notna()].copy()

df["is_delayed"] = (df["ARR_DELAY"] > 15).astype(int)

print(df[["ARR_DELAY", "is_delayed"]].head())
print(df["is_delayed"].value_counts())

df.to_csv(base_path / "flights_with_target.csv", index=False)