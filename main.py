from flask import Flask,render_template,redirect,request


app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/teacher')
def city_report():
   pass


@app.route('/signup')
def get_data(city_name):
    pass

if __name__=="__main__":
    app.run(debug=True)
