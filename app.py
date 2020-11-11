# Flaskからimportしてflaskを使えるようにする。
from flask import Flask, render_template, request, redirect
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
    places = c.fetchone
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
    c.close

    content = random.choice(content_li)

    return render_template("dbtest2.html", content=content[0], advice=content[1])

@app.route("/")
def template():
    return render_template("top.html")


@app.route("/question1")
def question():
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    contents = "SELECT content, advice FROM questions WHERE place_id = 1"
    c.execute(contents)
    contents = c.fetchall()
    content = contents[0]
    advice = contents[1]
    content = random.choice(contents)
    advice = random.choice(contents)
    c.close()

    return render_template("question1.html", content=content, place=advice)


@app.route("/question2")
def question2():
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    contents = "SELECT content, advice FROM questions WHERE place_id = 2"
    c.execute(contents)
    contents = c.fetchall()
    content = contents[0]
    advice = contents[1]
    content = random.choice(contents)
    advice = random.choice(contents)
    c.close()

    return render_template("question2.html", content=content, place=advice)


@app.route("/question3")
def question3():
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    contents = "SELECT content, advice FROM questions WHERE place_id = 3"
    c.execute(contents)
    contents = c.fetchall()
    content = contents[0]
    advice = contents[1]
    content = random.choice(contents)
    advice = random.choice(contents)
    c.close()

    return render_template("question3.html", content=content, place=advice)


@app.route("/question4")
def question4():
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    contents = "SELECT content, advice FROM questions WHERE place_id = 4"
    c.execute(contents)
    contents = c.fetchall()
    content = contents[0]
    advice = contents[1]
    content = random.choice(contents)
    advice = random.choice(contents)
    c.close()

    return render_template("question4.html", content=content, place=advice)


@app.route("/question5")
def question5():
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    contents = "SELECT content, advice FROM questions WHERE place_id = 5"
    c.execute(contents)
    contents = c.fetchall()
    content = contents[0]
    advice = contents[1]
    content = random.choice(contents)
    advice = random.choice(contents)
    c.close()

    return render_template("question5.html", content=content, place=advice)


@app.route("/question6")
def question6():
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    contents = "SELECT content, advice FROM questions WHERE place_id = 6"
    c.execute(contents)
    contents = c.fetchall()
    content = contents[0]
    advice = contents[1]
    content = random.choice(contents)
    advice = random.choice(contents)
    c.close()

    return render_template("question6.html", content=content, place=advice)


@app.route("/star", methods=["GET"])
def achievement_get():
    return render_template("star.html")


@app.route("/star", methods=["POST"])
def achievement_post():
    star = request.form.getlist("star")
    print(star)
    print(type(star))
    comment = request.form.get("comment")
    print(comment)
    conn = sqlite3.connect('flask.db')
    c = conn.cursor()
    c.execute("insert into star values(null,?,?)", (star[0], comment))

    conn.commit()
    c.close()
    return redirect("/")

    # # return redirect("/top")
    # return "送信完了"


# @app.route("/date")
# def date():
#     conn = sqlite3.connect('flasktest.db')
#     c = conn.cursor()
#     c.execute = "select content,advice,star,comment from questions where id = ?", (
#         id,)
#     date_list = []
#     for row in c.fetchall():
#         date_list.append(
#             {"content": row[0], "advice": row[1], "star": row[2], "comment": row[3]})
#     c.close()
#     return render_template('date.html', date_list=date_list)


@app.errorhandler(404)
def notfound(code):
    return "404ページだよ。ごめんね"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)

# join places on questions.place_id = places.id