from app import app

from flask import render_template,url_for



@app.route('/')
@app.route('/index')

def index():
    return render_template('principal.html')

@app.route('/contato')
def contato():
    return render_template('contato.html') 