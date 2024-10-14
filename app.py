from flask import Flask, render_template, request
import mensagens

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome") #atributo name do formulário

        mensagem = f"Olá {nome}!\nMensagem: {mensagens.obter_mensagem_aleatoria()}" #gera a mensagem

        return render_template("index.html", texto=mensagem) #renderizar a página com a mensagem

    return render_template("index.html") #renderiza a página inicial com o formulário

if __name__ == "__main__":
    app.run(debug=True)
