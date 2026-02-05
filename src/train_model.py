import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from src.preprocess import clean_text

data = pd.read_csv("data/sample_emails.csv")
data['email'] = data['email'].apply(clean_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['email'])
y = data['label']

model = LogisticRegression()
model.fit(X, y)

joblib.dump((model, vectorizer), "model/phishing_model.pkl")

print("Phishing detection model trained successfully")
