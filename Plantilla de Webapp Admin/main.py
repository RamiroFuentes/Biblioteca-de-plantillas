from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/404')
def notFound():
    title = "Solar Tracker Admin - 404"
    return render_template('404.html',title=title)

@app.route('/blank')
def blank():
    title = "Solar Tracker Admin - blank"
    return render_template('blank.html',title=title)

@app.route('/charts')
def charts():
    title = "Solar Tracker Admin - charts"
    return render_template('charts.html',title=title)

@app.route('/forgot-password')
def forgotPassword():
    title = "Solar Tracker Admin - Forgot passwordr"
    return render_template('forgot-password.html',title=title)   

@app.route('/index')
def index():
    title = "Solar Tracker Admin - index"
    return render_template("index.html",title=title)

@app.route('/login')
def login():
    title = "Solar Tracker Admin - login"
    return render_template("login.html",title=title)

@app.route('/register')
def register():
    title = "Solar Tracker Admin - Register"
    return render_template('register.html',title=title)

@app.route('/tables')
def tables():
    title = "Solar Tracker Admin - tables"
    return render_template('tables.html',title=title)

@app.route('/layout')
def layout():
    title = "Solar Tracker Admin - layout"
    return render_template('layout.html',title=title)

@app.route('/prueba')
def prueba():
    title = "Solar Tracker Admin - Prueba"
    return render_template('Prueba.html',title=title)
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)