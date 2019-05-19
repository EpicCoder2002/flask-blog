from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>hello World !</h1><h2>Home Page</h2>"

@app.route("/about")
def about():
    return "<h1>hello World !</h1><h2>About Page</h2>"

if __name__ == '__main__':
    app.run(debug=True)