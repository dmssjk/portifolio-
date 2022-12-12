from app import app

from flask import render_template,url_for



@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html') 

@app.route('/quemsou')
def quemsou():
    return render_template('quemsou.html') 

@app.route('/prof')
def profiional():
    return render_template('prof.html') 

