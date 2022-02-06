from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/aboutme")
def about():
    return render_template("aboutme.html")


@app.route("/services")
def about():
    return render_template("services.html")


@app.route("/contact")
def about():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
