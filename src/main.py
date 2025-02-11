from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from MyApp to you - Dev-staging-prod environment!... ...00 - v3.4.10- used a newer way to update the version taging and updating the vversion detection to major, minor and patch, label detection using API"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)