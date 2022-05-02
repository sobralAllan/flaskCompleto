from flask import Flask, render_template #importando o flask para a sua criação

app = Flask(__name__) #App é o nome da variável principal, padrão para início do flask
#Toda página no flask tem o route e a função, a route é o caminho depois do link
#Função o que será exibido na página.

@app.route("/")#Decorator no python, linha de código com objetivo de atribuir funcionalidade para o que está abaixo
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")#O que escrever vai aparecer na tela
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)#Colocar o site no ar, Debug == True é ativar o debug, toda alteração ele já altera automaticamente

# servidor do heroku - Totalmente Gratuito
# Configurar o procfile
# requirements