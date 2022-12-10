from flask import Flask, render_template, request, redirect, session
from user_model import User
app = Flask(__name__)

app.secret_key = 'stealthKey'

#* ================= HOME VIEW ==================

@app.route('/')
def readAll():
  currUsers = User.get_all()
  return render_template("readAll.html", currUsers=currUsers)

#* ================= SHOW FORM (VIEW) & CREATE USER (ACTION) =======================

#* SHOW FORM (VIEW)
@app.route('/user/new')
def userForm():
  User.get_all()
  return render_template("create.html")

#* CREATE USER GET FORM DATA FROM (ACTION)                  
@app.route('/user/create', methods=["post"])
def form_data_create_user():
  
  #* PASS DICTIONARY FROM request.form TO CLASS METHOD create_user
  User.create_user(request.form)
  
  return redirect("/")

if __name__=="__main__":   
    app.run(debug=True)    