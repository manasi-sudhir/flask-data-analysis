from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on GCP VM!"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
