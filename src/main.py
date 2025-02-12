from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from MyApp to you - Dev-staging-prod environment!!...  - v3.4.10- used a newer way to build the image and update PR labels lets make it better"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)