from flask import Flask, render_template, request
import numpy as np
import pickle
import sklearn

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    message = ""
    if request.method=='POST':
        character = np.array([[
            request.form['area'],
            request.form['bedrooms'],
            request.form['bathrooms'],
            request.form['stories'],
            request.form['parking']
        ]])
        file = open('housingModel.pickle', "rb")
        model = pickle.load(file)
        file.close()
        message = f"The approximate price of the house is INR {round(model.predict(character)[0])}"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()