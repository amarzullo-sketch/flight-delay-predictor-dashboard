from pathlib import Path
import pandas as pd

base_path = Path(__file__).resolve().parent.parent

input_path = base_path / "Cleaned Data" / "clean_flights.csv"

df = pd.read_csv(input_path)

# X = features, y = target
X = df.drop(columns=["is_delayed"])
y = df["is_delayed"]

# turn text columns into numbers
X = pd.get_dummies(X, drop_first=True)

print("X shape:", X.shape)
print("y shape:", y.shape)
print(X.head())
print(y.head())