from flask import Flask, render_template
from requests import request

app = Flask(__name__)

api_answer = request('get', 'https://api.npoint.io/ba077311bd9916cde9a7')

@app.route('/')
def index():
    return render_template("index.html", posts=api_answer.json())

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def post(id):
    requested_post = None
    for blog_post in api_answer.json():
        if blog_post["id"] == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True) 