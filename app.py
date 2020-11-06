# Flaskからimportしてflaskを使えるようにする。
from flask import Flask, render_template
import sqlite3
import random

# appっていう名前でFlaskアプリを作っていくよーみたいな
app = Flask(__name__)

# 秘密鍵
app.secret_key = "kimazuin"


@app.route("/dbtest")
def dbtest():
    # flask.dbに接続
    conn = sqlite3.connect("flask.db")
    # 中身が見られるようにする
    c = conn.cursor()
    # SQL文の実行
    c.execute("select * from places")
    c.execute("select * from places")
    # 取ってきたレコードを格納 fetch=取ってくるという意味の英単語
    places = c.fetchall()
    # データベース接続終了
    c.close()
    
    return render_template("dbtest.html", places=places)

@app.route("/dbtest2")
def dbtest2():
    # flasktest.dbに接続します
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    content_li = "SELECT content,advice FROM questions where place_id=1;"
    # sql文を実行
    c.execute(content_li)
    # 取ってきた内容を変数に格納する
    content_li = c.fetchall()
    # データベースの接続終了
    c.close()
    
    content=random.choice(content_li)

    return render_template("dbtest2.html", content=content[0], advice=content[1])

@app.route("/")
def helloWorld():
    return "HelloWorld."


@app.route("/top")
def template():
    return render_template("top.html")


@app.route("/question")
def question():
    return render_template("question.html")


@app.route("/star")
def achievement():
    return render_template("star.html")


@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。ごめんね"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)
