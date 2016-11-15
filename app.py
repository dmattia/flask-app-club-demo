from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data")
def data():
  d = {
    "key1": 5,
    "hello": 6,
    "user3": 9,
    "pierce": -1
  }
  return jsonify(**d) 

@app.route("/html")
def home():
  return render_template("index.html", name="Pierce")

if __name__ == "__main__":
    app.run()
