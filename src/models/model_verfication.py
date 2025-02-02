import joblib
import numpy as np

# Load saved artifacts
loaded_scaler = joblib.load("../../models/scaler.pkl")
loaded_model = joblib.load("../../models/classifier.pkl")

# Test prediction
test_input = np.array([5, 166, 72, 19, 175, 25.8, 0.587, 51]).reshape(1, -1)
scaled_input = loaded_scaler.transform(test_input)
prediction = loaded_model.predict(scaled_input)

print("\nVerification Test:")
print(f"Input: {test_input[0]}")
print(f"Prediction: {'Diabetic' if prediction[0] == 1 else 'Not Diabetic'}")
