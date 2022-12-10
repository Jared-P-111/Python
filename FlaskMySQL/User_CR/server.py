from flask import Flask, render_template, request, redirect, session
from user_model import User
app = Flask(__name__)

app.secret_key = 'stealthKey'

@app.route('/')
def index():
  User.get_all()
  return render_template("create.html")

@app.route('/users')
def readAll():
  currUsers = User.get_all()
  return render_template("readAll.html", currUsers=currUsers)

if __name__=="__main__":   
    app.run(debug=True)    