from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route("/")
def home():
    return "<h1>Welcome to my website!</h1>"