import os
import Model
import Data
import OCRThai
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()
port = os.getenv("PORT")
if port is None:
    port = 5000

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello, Flask!!!!"


@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text")
    if text:
        return predict_by_text(text)
    image = request.files.get("image")
    if image:
        text = OCRThai.image_to_string(image.stream)
        return predict_by_text(text)
    return "No input provided!"

@app.route("/metrics", methods=["GET"])
def accuracy():
    return Model.get_metrics(model, vectorizer)



def predict_by_text(text):
    tokens = Data.preprocess_data(text)
    x_new = vectorizer.transform([" ".join(tokens)])
    y_new = model.predict(x_new)
    return {
        "predicted_label": y_new.tolist()[0],
    }


if __name__ == "__main__":
    vectorizer, model = Model.load_model()
    app.run(port=port)
