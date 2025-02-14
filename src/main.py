from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from MyApp to you - Dev-staging-prod environment!! !!@@ ^^^^!... ...0000++++==%%% - v3.4.13- used a newer way to build the image and update PR labels accurately"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)