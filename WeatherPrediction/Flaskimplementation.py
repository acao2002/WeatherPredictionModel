from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])

def index():
    last_name = ''
    first_name =''
    if request.method == "POST": 
       # getting input with name = fname in HTML form 
       first_name = request.form.get("fname") 
       # getting input with name = lname in HTML form  
       last_name = request.form.get("lname")  

    return render_template('index.html',variable =first_name,variable2 = last_name)

if __name__ == "__main__":
    app.run(debug = True)