# Flaskからimportしてflaskを使えるようにする。
from flask import Flask, render_template
import sqlite3

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
    places = c.fetchone()
    # データベース接続終了
    c.close()
    
    return render_template("dbtest.html", places=places)

@app.route("/dbtest2")
def dbtest2():
    # flasktest.dbに接続します
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    ques = "SELECT id, content, advice FROM questions;"
    # sql文を実行
    c.execute(ques)
    print("OK")
    # 取ってきた内容を変数に格納する
    ques = c.fetchone()
    # データベースの接続終了
    c.close()

    ques = ques[1]
    print(ques)
    return render_template("dbtest2.html", ques=ques)

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
