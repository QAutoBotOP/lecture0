# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     headline = "Oi, govna!"
#     return render_template("index.html", headline=headline)

# @app.route("/<string:name>")
# def hello(name):
#     return f"Hello, {name}!"

# import datetime

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     now = datetime.datetime.now()
#     new_year = now.month == 1 and now.day == 1
#     # text = "Yes" if new_year else "NO"
#     return render_template("index.html", new_year=new_year)


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Aelis", "Benedict", "Charles"]
    return render_template("index.html", names=names)