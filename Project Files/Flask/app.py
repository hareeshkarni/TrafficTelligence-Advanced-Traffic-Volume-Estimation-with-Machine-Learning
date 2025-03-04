import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import flask
from flask import render_template,request
import pickle


app = flask.Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])

def predict():
    temp=float(request.form["temp"])
    rain=float(request.form["rain"])
    snow=float(request.form["snow"])
    weather=int(request.form["weather"])
    day=int(request.form["day"])
    month=int(request.form["month"])
    year=int(request.form["year"])
    hour=int(request.form["hour"])
    minutes=int(request.form["minutes"])
    seconds=int(request.form["seconds"])

    input_data=np.array([[temp,rain,snow,weather,day,month,year,hour,minutes,seconds]])
    prediction=model.predict(input_data)[0]
    return render_template("index.html",prediction=f"Predicted traffic volume:{prediction:.2f}")

if __name__=="__main__":
    app.run(debug=True)