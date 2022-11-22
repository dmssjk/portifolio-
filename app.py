from flask import Flask, render_template          ##importando o flask  e o render template

app = Flask(__name__)  ## ver video para entender oque isso faz! https://youtu.be/150-dpYG1pg 



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/principal") ## principal
def principal():   
    return render_template('principal.html')

@app.route("/familia") ## familia
def familia():    
    return render_template('familia.html')

@app.route("/contato") ## contato
def contato():    
    return render_template('contato.html')

@app.route("/trabalhos") ## trabalhos
def trabalhos():    
    return render_template('trabalhos.html')    



if __name__ == '__main__':## colocar o site no ar
    app.run(debug=True )  ## ativar o debug do site ou seja ele exibe automaticamente as alteracoes do codigo no navegador


