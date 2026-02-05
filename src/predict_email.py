import joblib
from src.preprocess import clean_text

model, vectorizer = joblib.load("model/phishing_model.pkl")

email = input("Enter email content: ")
cleaned = clean_text(email)
vectorized = vectorizer.transform([cleaned])

prediction = model.predict(vectorized)

print("Prediction:", prediction[0])
