from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'stealthKey'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
  session["name"] = request.form["name"]
  session["dojo_location"] = request.form["dojo_location"]
  session["language"] = request.form["language"]
  session["comments"] = request.form["comments"]
  
  print(request.form)
  
  return render_template("results.html")

if __name__=="__main__":   
    app.run(debug=True)    
    