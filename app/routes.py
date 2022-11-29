from app import app

from flask import render_template,url_for



@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html') 

@app.route('/familia')
def familia():
    return render_template('familia.html') 

@app.route('/trabalhos')
def trabalhos():
    return render_template('trabalhos.html') 

