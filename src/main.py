from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hello from MyApp to you - Dev-staging-prod environment!... ...00 - v3.4.8- used a newer way to update the version taging"
=======
    return "Hello from MyApp to you - Dev-staging-prod environment!... ...00 - v3.4.7- used a newer way to update the version taging"
>>>>>>> dev

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)