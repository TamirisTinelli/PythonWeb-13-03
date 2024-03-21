from flask import Flask, render_template

app = Flask("Olá")

@app.route("/")
def ola():
    return "Olá mundo, grande mundo"

@app.route("/alunos")
def alunos():
    return render_template("hello.html")