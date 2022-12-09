from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'stealthKey'

@app.route('/')
def index():
  return render_template("create.html")

if __name__=="__main__":   
    app.run(debug=True)    