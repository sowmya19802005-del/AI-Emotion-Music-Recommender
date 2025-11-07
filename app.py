import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# -------------------------------
# 🧩 STEP 1: Load and Combine Data
# -------------------------------

# Each file has text;emotion and no headers
train = pd.read_csv("train1.csv", sep=";", names=["text", "emotion"])
test = pd.read_csv("test1.csv", sep=";", names=["text", "emotion"])
val = pd.read_csv("val1.csv", sep=";", names=["text", "emotion"])

# Combine all into one dataframe
data = pd.concat([train, test, val], axis=0).reset_index(drop=True)
print("✅ Data loaded successfully!")
print("Total samples:", len(data))
print(data.head())

# -----------------------------------
# 🧠 STEP 2: Vectorize and Train Model
# -----------------------------------
X = data["text"]
y = data["emotion"]

vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=200)
model.fit(X_vec, y)

# -----------------------------------
# 💾 STEP 3: Save Model and Vectorizer
# -----------------------------------
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved successfully!")
