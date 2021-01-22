from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html',variable ="hello",variable2 ="hello again")

if __name__ == "__main__":
    app.run(debug = True)