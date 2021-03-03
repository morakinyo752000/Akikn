from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def sign():
#     return render_template("sign(2).html")
#
@app.route('/signup.html/')
def signup():
    return render_template("signup.html")

# @app.route(('/home/')
# def home():
#     return render_template("home.html")

if __name__== "__main__   ":
    app.run(debug=True)