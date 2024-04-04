from flask import Flask, render_template, g, request, redirect, session, url_for, flash, abort
import sqlite3

app = Flask("blog")
DATABASE = "banco.bd"
SECRET_KEY = "1234"

app.config.from_object(__name__)

def conectar():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.bd = conectar() 

@app.teardown_request
def teardown_request(f):
    g.bd.close()

@app.route("/")
def blog():
    sql = "SELECT titulo, texto, data_criacao FROM posts ORDER BY id DESC"

    resultado = g.bd.execute(sql)

    post = [{"titulo": "Meu titulo4", "texto": "Meu texto", "data_criacao":"27/03/2024"},
             {"titulo": "Meu titulo2", "texto": "Meu texto2", "data_criacao":"26/03/2024"}]

    #post = []
    for titulo, texto, data_criacao in resultado.fetchall():
        post.append({
            "titulo":titulo, 
            "texto":texto, 
            "data_criacao":data_criacao
           })
    return render_template("exibir_posts.html", post=post)

@app.route("/login",  methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")