from flask import Flask, render_template, url_for

#Name badalna hai kya?
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#Debug abhi ke liye on rakha hai
if __name__ == "__main__":
    app.run(debug=True)