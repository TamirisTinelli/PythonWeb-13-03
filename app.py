from flask import Flask, render_template

app = Flask("blog")

@app.route("/")
def blog():
    posts = [{"titulo": "Meu titulo", "texto": "Meu texto", "data_criacao":"27/03/2024"},
             {"titulo": "Meu titulo2", "texto": "Meu texto2", "data_criacao":"26/03/2024"}]
    return render_template("exibir_posts.html", post=posts)