import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("training_data.csv")

X = df["question"]
y = df["intent"]

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)

model.fit(X_vectorized, y)

joblib.dump(model, "intent_model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("Model trained successfully")