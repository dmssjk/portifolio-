from flask import Flask, render_template          ##importando o flask  e o render template

app = Flask(__name__)  ## ver video para entender oque isso faz! https://youtu.be/150-dpYG1pg 



## to pagina tem uma rota e uma funcao, sendo a rota o caminho e a funcao
@app.route("/") ## rota  ## index 
def index():    ## funcao
    return render_template()

@app.route("/principal") ## principal
def principal():    
    return render_template()

@app.route("/familia") ## familia
def familia():    
    return render_template('familia.html')

@app.route("/contatos") ## contatos
def contatos():    
    return render_template('contato.html')

@app.route("/trabalhos") ## trabalhos
def trabalhos():    
    return render_template('trabalhos.html')    


  

## colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) ## ativar o debug do site ou seja ele exibe automaticamente as alteracoes do codigo no navegador