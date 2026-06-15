from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
@app.route('/login')
def login():
    return render_template('login.html')

# Load Dataset
data = pd.read_csv("dataset.csv")

# Features and Target
X = data.drop("disease", axis=1)
y = data["disease"]

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Recommendations
recommendations = {

    "Flu": ["Take adequate rest", "Drink plenty of fluids", "Monitor body temperature"],
    "Cold": ["Drink warm water", "Take proper rest", "Avoid cold foods"],
    "Malaria": ["Consult a doctor immediately", "Take prescribed medication", "Stay hydrated"],
    "Allergy": ["Avoid allergens", "Take antihistamines if prescribed", "Consult a doctor if severe"],
    "Food Poisoning": ["Drink ORS solution", "Eat light foods", "Stay hydrated"],
    "Migraine": ["Rest in a quiet room", "Avoid bright lights", "Stay hydrated"],
    "Dengue": ["Monitor platelet count", "Drink plenty of fluids", "Consult doctor immediately"],
    "Cough": ["Drink warm fluids", "Avoid cold drinks", "Get enough rest"],
    "Typhoid": ["Take prescribed antibiotics", "Eat nutritious food", "Drink safe water"],
    "Stomach Infection": ["Stay hydrated", "Eat bland foods", "Consult doctor if symptoms worsen"],
    "Healthy": ["Maintain healthy habits", "Exercise regularly", "Drink sufficient water"],
    "Viral Fever": ["Get adequate rest", "Drink fluids", "Monitor temperature"],
    "Fever": ["Take rest", "Drink water", "Monitor symptoms"],
    "Sinus Infection": ["Use steam inhalation", "Stay hydrated", "Consult a doctor if persistent"],
    "Covid-19": ["Isolate yourself", "Wear a mask", "Consult healthcare provider"],
    "Food Allergy": ["Avoid triggering foods", "Take prescribed medication", "Seek medical help if severe"],
    "Chickenpox": ["Avoid scratching", "Take adequate rest", "Stay hydrated"],
    "Bronchitis": ["Avoid smoking", "Drink warm fluids", "Get enough rest"],
    "Throat Infection": ["Gargle with warm salt water", "Drink warm liquids", "Avoid cold foods"],
    "Stress Headache": ["Practice relaxation techniques", "Get enough sleep", "Reduce stress"],
    "Gastric Problem": ["Avoid spicy foods", "Eat small meals", "Drink water regularly"],
    "Respiratory Infection": ["Rest adequately", "Stay hydrated", "Consult doctor if symptoms worsen"],
    "Severe Viral Infection": ["Consult a doctor immediately", "Take adequate rest", "Follow medical advice"],
    "Acidity": ["Avoid spicy foods", "Eat smaller meals", "Avoid lying down after eating"],
    "Eye Flu": ["Avoid touching eyes", "Use clean towels", "Consult an eye specialist"],
    "Asthma": ["Avoid triggers", "Use inhaler if prescribed", "Consult doctor regularly"],
    "Pneumonia": ["Seek medical treatment", "Take prescribed medication", "Get sufficient rest"],
    "Motion Sickness": ["Avoid heavy meals before travel", "Focus on a fixed point", "Stay hydrated"],
    "Normal Fever": ["Take rest", "Drink fluids", "Monitor temperature"],
    "Tiredness": ["Get adequate sleep", "Eat nutritious food", "Stay hydrated"]
}

# Landing Page
@app.route('/')
def home():
    return render_template('landing.html')

# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Predict Page
@app.route('/predict')
def predict():
    return render_template('predict.html')

# Result Page
@app.route('/result', methods=['POST'])
def result():

    fever = int(request.form['fever'])
    cough = int(request.form['cough'])
    headache = int(request.form['headache'])
    vomiting = int(request.form['vomiting'])
    fatigue = int(request.form['fatigue'])
    body_pain = int(request.form['body_pain'])
    sore_throat = int(request.form['sore_throat'])
    runny_nose = int(request.form['runny_nose'])
    skin_rash = int(request.form['skin_rash'])
    joint_pain = int(request.form['joint_pain'])
    breathing_problem = int(request.form['breathing_problem'])
    loss_of_appetite = int(request.form['loss_of_appetite'])

    symptoms = pd.DataFrame([{
        "fever": fever,
        "cough": cough,
        "headache": headache,
        "vomiting": vomiting,
        "fatigue": fatigue,
        "body_pain": body_pain,
        "sore_throat": sore_throat,
        "runny_nose": runny_nose,
        "skin_rash": skin_rash,
        "joint_pain": joint_pain,
        "breathing_problem": breathing_problem,
        "loss_of_appetite": loss_of_appetite
    }])

    prediction = model.predict(symptoms)[0]

    confidence = 92

    tips = recommendations.get(
        prediction,
        ["Consult a healthcare professional"]
    )

    return render_template(
        'result.html',
        prediction=prediction,
        confidence=confidence,
        tips=tips
    )

if __name__ == '__main__':
    app.run(debug=True)