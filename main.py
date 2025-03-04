from flask import Flask, render_template

app = Flask("website")

@app.route("/home")
def home():
    return render_template("tutorial.html")

if __name__ == "__main__":
    app.run(debug=True)