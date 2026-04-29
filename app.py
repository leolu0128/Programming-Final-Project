from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>這是我的期末專題網站</h1><p>目前運行中！</p>"

if __name__ == '__main__':
    app.run(debug=True)