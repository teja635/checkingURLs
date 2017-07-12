from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def main():
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        urls = [i for i in c.execute('SELECT * FROM URLS')]
        print(urls)
        return render_template('index.html', links=urls)

if __name__ == "__main__":
        app.run(debug=True)
