# importing necessary libraries and functions
import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__) #Initialize the flask App
model = load('mymodel.joblib')

@app.route('/') # Homepage
def home():
    return render_template('./index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    line = request.form.getlist('line_name')[0]
    stop = request.form.getlist('stop_number')[0]

    input = Switcher(line)
    number = int(stop)
    input.append(number)
    
    input = np.array(input).reshape(1,-1)

    prediction = model.predict(input)
    prediction = np.round(prediction,2)
    prediction = prediction[0]

    return render_template('index.html', prediction_text='Predicted Delay for Stop {} on the {}: {} minute(s)'.format(stop,line,prediction)) # rendering the predicted result

def Switcher(argument):
    switcher = {
        'Atl. City Line': [1,0,0,0,0,0,0,0,0,0,0],
        'Bergen Co. Line ': [0,1,0,0,0,0,0,0,0,0,0],
        'Gladstone Branch': [0,0,1,0,0,0,0,0,0,0,0],
        'Main Line': [0,0,0,1,0,0,0,0,0,0,0],
        'Montclair-Boonton': [0,0,0,0,1,0,0,0,0,0,0],
        'Morristown Line': [0,0,0,0,0,1,0,0,0,0,0],
        'No Jersey Coast': [0,0,0,0,0,0,1,0,0,0,0],
        'Northeast Corrdr': [0,0,0,0,0,0,0,1,0,0,0],
        'Pascack Valley': [0,0,0,0,0,0,0,0,1,0,0],
        'Princeton Shuttle': [0,0,0,0,0,0,0,0,0,1,0],
        'Raritan Valley': [0,0,0,0,0,0,0,0,0,0,1],
    }
    return switcher.get(argument, [-1])

if __name__ == "__main__":
    app.run(debug=True)