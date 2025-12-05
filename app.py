from flask import Flask,render_template,request,url_for
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('crop.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods =['GET','POST'])
def prediction ():
    if request.method == 'POST':
        try:
            nitrogen = int(request.form['Nitrogen'])
            phosphorus = int(request.form['phosphorus'])
            rain = int(request.form['rainfall'])
            temperature = int(request.form['temperature'])
            humidity = int(request.form['humility'])

            outcome = np.array([[nitrogen, phosphorus, rain, temperature, humidity]])

            output = model.predict(outcome)
            return render_template('index.html', result =f'plant {output}')
        except Exception as e:
            return render_template('index.html', result = f'{e}')
if __name__ == '__main__':
    app.run(debug=True)