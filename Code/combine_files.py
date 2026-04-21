# Optional script: only use this if rebuilding combined_flights.csv
# from the original raw monthly CSV files.

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "raw data"
OUTPUT_DIR = BASE_DIR / "Combined data"
OUTPUT_DIR.mkdir(exist_ok=True)

files = list(RAW_DIR.rglob("*.csv"))
print("Found files:", files)

if not files:
    raise FileNotFoundError(f"No CSV files found in: {RAW_DIR}")

df = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)

output_path = OUTPUT_DIR / "combined_flights.csv"
df.to_csv(output_path, index=False)

print(f"Saved combined file to: {output_path}")
print(f"Final row count: {len(df)}")