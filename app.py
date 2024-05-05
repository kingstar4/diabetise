from flask import Flask, render_template, request
import numpy as np
import pickle


app = Flask(__name__, template_folder = 'templates', static_folder = 'static')

model = pickle.load(open('Diabetes_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUIS
    '''
    if request.method == 'POST':

      preg = request.form.get('preg')
      glu = int(request.form.get('glu'))
      bp = int(request.form.get('BP'))
      sk = int(request.form.get('SK'))
      il = int(request.form.get('IL'))
      bmi = float(request.form.get('BMI'))
      dpf = float(request.form.get('DPF'))
      age = int(request.form.get('AGE'))
    
      prediction = model.predict([[preg,glu ,bp,sk,il,bmi,dpf,age]])

    output = prediction[0]

    if output ==1:
       return render_template('index.html', prediction_text='YOU ARE DIABETIC  ')

    else:
     return render_template('index.html', prediction_text='YOU ARE NOT DIABETIC')

if __name__ == "__main__":
  app.run(debug = True)