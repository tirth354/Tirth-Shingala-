import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("transactions.csv")

X = data[
    [
        "amount",
        "hour",
        "new_device",
        "location_mismatch"
    ]
]

y = data["fraud"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully.")