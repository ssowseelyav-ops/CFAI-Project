from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Load Dataset
data = pd.read_csv("dataset.csv")

X = data.drop("disease", axis=1)
y = data["disease"]

# Train Model
model = DecisionTreeClassifier()
model.fit(X, y)

# LOGIN PAGE
@app.route('/')
def login():
    return render_template("login.html")

# SYMPTOM PAGE
@app.route('/predict')
def predict():

    name = request.args.get('name')
    age = request.args.get('age')
    sex = request.args.get('sex')

    return render_template(
        "predict.html",
        name=name,
        age=age,
        sex=sex
    )

# RESULT PAGE
@app.route('/result', methods=['POST'])
def result():

    name = request.form['name']

    fever = int(request.form['fever'])
    cough = int(request.form['cough'])
    headache = int(request.form['headache'])
    vomiting = int(request.form['vomiting'])
    fatigue = int(request.form['fatigue'])

    symptoms = [[fever, cough, headache, vomiting, fatigue]]

    prediction = model.predict(symptoms)[0]

    return render_template(
        "result.html",
        prediction=prediction,
        name=name
    )

if __name__ == '__main__':
    app.run(debug=True)