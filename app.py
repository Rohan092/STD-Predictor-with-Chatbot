from flask import Flask, render_template, request
import pickle
import numpy as np
import cohere
from flask import jsonify

app = Flask(__name__)
co = cohere.Client("SXxWHnk5asKNWLfw7dZBw7S3IfptPbN2CaE1vdsN")
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index3.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([np.array(features)])
    result = "STD Positive" if prediction[0] == 1 else "STD Negative"
    print(prediction)
    return jsonify(prediction_text=result)

@app.route("/furiosa")
def furiosa():
    return render_template("index3.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    response = chat_with_Furiosa(msg)
    return response

def chat_with_Furiosa(text):
    if text.lower() in ["quit", "exit", "bye"]:
        return "Goodbye!"
    response = co.generate(
        model="command",
        prompt=text,
        max_tokens=500,
        temperature=0.7,
        stop_sequences=["END"]
    )
    return response.generations[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)