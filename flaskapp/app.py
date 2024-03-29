from flask import Flask, render_template, jsonify, request, redirect, url_for

'''
makes a variable called 'app' that is the 
source of this web app so i can tie differnt web functions or routesto it
'''
app = Flask(__name__)
'''
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key",
    MAIL_SERVER = "localhost",
    MAIL_PORT = 25,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = '#',
    MAIL_PASSWORD = '#',
))
EX: 
temp= "haiiaiaiaaiai "
render_template("index.html", temp) 
IN HTML, I use {{temp}}
'''
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Resume")
def resume():
    return redirect("https://www.terpconnect.umd.edu/~sanjays/Personal-Website%20Externals/Sanjay_Srikumar_Resume.pdf")

@app.route("/<string:name>")
def general(name):
    return ("<h1>This Page Does Not Exist</h1>")

@app.route("/about")
def about():
    return render_template("about_me.html")

@app.route("/Projects")
def projects():
    return render_template("Projects.html")
@app.route("/Contact")
def contact():
    return render_template("contact.html")

