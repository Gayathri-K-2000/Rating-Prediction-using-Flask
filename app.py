from flask import Flask, jsonify
import joblib
app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    
    reviews = request.form['reviews']
    size = request.form['size']
    installs = request.form['installs']
    pre=""
    model = joblib.load("playstore_model.sav")

    pred = model.predict([[reviews, size, installs]])
    p=pred.tolist()
    for ele in p:
        pre += str(ele)
    return jsonify(rating= pre)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
