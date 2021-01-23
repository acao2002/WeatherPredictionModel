from flask import Flask , render_template, request, redirect, url_for
app = Flask(__name__)
from WeatherPrediction import weather

@app.route('/', methods = ["GET", "POST"])

def index():
    state = 0
    days =0
    sunny = 0 
    rainy = 0 
    cloudy = 0
    if request.method == "POST": 
        if 'submitname' in request.form:
        # getting input with name = fname in HTML form 
                state = int(request.form.get("fname") )
        # getting input with name = lname in HTML form  
                days = int(request.form.get("lname") )
                Weather = weather() 
                prediction = Weather.predict(state,days) 
                sunny = prediction[0]*100
                rainy = prediction[1]*100
                cloudy = prediction[2]*100
        else: 
            pass
    return render_template('index.html',var = sunny ,var1 = rainy,var2 = cloudy)

if __name__ == "__main__":
    app.run(debug = True)