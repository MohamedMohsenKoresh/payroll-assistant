import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


df = pd.read_csv("data/training_data.csv")

df = df.drop_duplicates()

X = df["question"]
y = df["intent"]


vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    lowercase=True
)

X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(
    X_vectorized,
    y
)

joblib.dump(
    model,
    "models/intent_model.joblib"
)

joblib.dump(
    vectorizer,
    "models/vectorizer.joblib"
)

print("Model trained successfully")