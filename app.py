from flask import Flask

# Init the Flask
app = Flask(__name__)

#  base_url/
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/another_route")
def another_route():
    return "This is another route"

@app.route("/one_more_route")
def one_more_route():
    return "One more route"