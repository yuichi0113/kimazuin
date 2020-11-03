# Flaskからimportしてflaskを使えるようにする。
from flask import Flask, render_template
import sqlite3

# appっていう名前でFlaskアプリを作っていくよーみたいな
app = Flask(__name__)

# 秘密鍵
app.secret_key = "kimazuin"

@app.route("/")
def helloWorld():
    return "HelloWorld."

@app.route("/top")
def template():
    return render_template("top.html")

@app.route("/star")
def achievement():
    return render_template("star.html")

@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。ごめんね"

if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)
