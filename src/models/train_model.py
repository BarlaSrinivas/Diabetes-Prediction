#


#####
#####
#####

# Importing the Dependencies
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import joblib

# Data Collection and Analysis
diabetes_dataset = pd.read_csv("../../data/raw/diabetes.csv")

# Data Preprocessing
X = diabetes_dataset.drop(columns="Outcome", axis=1)
Y = diabetes_dataset["Outcome"]

# Data Standardization
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
X = standardized_data

# Train Test Split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

# Model Training
classifier = svm.SVC(kernel="linear")
classifier.fit(X_train, Y_train)

# Model Evaluation
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print(f"Final Model Accuracy: {test_data_accuracy:.2f}")

# Save Artifacts
joblib.dump(scaler, "../../models/scaler.pkl")
joblib.dump(classifier, "../../models/classifier.pkl")

print("Model and scaler saved successfully!")
