from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load models with error handling
try:
    scaler = joblib.load("models/scaler.pkl")
    classifier = joblib.load("models/classifier.pkl")
except FileNotFoundError:
    raise SystemExit("Model files missing! Run training script first.")
except Exception as e:
    raise SystemExit(f"Error loading models: {str(e)}")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Validate input
        features = [float(x) for x in request.form.values()]
        if len(features) != 8:
            raise ValueError("Exactly 8 health parameters required")

        # Process input
        input_data = np.array(features).reshape(1, -1)
        scaled_data = scaler.transform(input_data)
        prediction = classifier.predict(scaled_data)

        # Return result
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        return render_template("index.html", prediction_text=f"Diagnosis: {result}")

    except ValueError as ve:
        return render_template("index.html", prediction_text=f"Input Error: {str(ve)}")
    except Exception as e:
        return render_template(
            "index.html", prediction_text="Prediction Error. Check input values."
        )


if __name__ == "__main__":
    app.run(debug=False)  # Disable debug in production
