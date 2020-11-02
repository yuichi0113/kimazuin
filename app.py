# Flaskからimportしてflaskを使えるようにする。
from flask import Flask
import sqlite3

# appっていう名前でFlaskアプリを作っていくよーみたいな
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "HelloWorld."

if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=True)
