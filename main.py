from flask import Flask , request , render_template
import requests

app = Flask(__name__)


@app.route('/temperature' , methods = ['POST'])
def temperature():
    zip_code = request.form['zipcode']
    r = requests.get('http://samples.openweathermap.org/data/2.5/weather?zip='+zip_code+',IN&appid=c3dc653f46db45c8910c14ad624e882d')
    r_json = r.json()
    temp_kel = float(r_json["main"]["temp"])
    return render_template('temperature.html' , temp = temp_kel)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug = True)
