from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "Combined data" / "combined_flights.csv"
OUTPUT_DIR = BASE_DIR / "Cleaned Data"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(INPUT_PATH)

df["is_delayed"] = (df["ARR_DELAY"] > 15).astype(int)

output_path = OUTPUT_DIR / "flights_with_target.csv"
df.to_csv(output_path, index=False)

print(f"Saved file to: {output_path}")
print(df[["ARR_DELAY", "is_delayed"]].head())
print(f"Final row count: {len(df)}")