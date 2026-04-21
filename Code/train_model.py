from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

base_path = Path(__file__).resolve().parent.parent
input_path = base_path / "Cleaned Data" / "selected_flights.csv"

df = pd.read_csv(input_path)

X = df.drop(columns=["is_delayed"])
y = df["is_delayed"]

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

BASE_DIR = Path(__file__).resolve().parent.parent
image_path = BASE_DIR / "confusion_matrix.png"

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.title("Confusion Matrix")
plt.savefig(image_path, bbox_inches="tight")
plt.close()

print(f"Saved confusion matrix image to: {image_path}")