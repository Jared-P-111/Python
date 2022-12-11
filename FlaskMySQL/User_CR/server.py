from flask import Flask, render_template, request, redirect, session
from user_model import User
app = Flask(__name__)

app.secret_key = 'stealthKey'

#* ================= HOME VIEW ==================

@app.route('/')
def readAll():
  currUsers = User.get_all()
  return render_template("readAll.html", currUsers=currUsers)

#* ================ ONE USER VIEW ===============

@app.route('/user/<int:id>')
def getUser(id):
  user = User.get_one_user(id)
  print("USER ===========================>      ", user)
  return render_template("readOne.html", user=user)

#* ================= SHOW FORM (VIEW) & CREATE USER (ACTION) =======================

#* SHOW FORM (VIEW)
@app.route('/user/new')
def userForm():
  User.get_all()
  return render_template("create.html")

#* CREATE USER GET FORM DATA FROM (ACTION)                  
@app.route('/user/create', methods=["POST"])
def form_data_create_user():
  
  #* PASS DICTIONARY FROM request.form TO CLASS METHOD create_user
  User.create_user(request.form)
  
  return redirect("/")

#* =================== DELETE USER ======================

@app.route('/delete/<int:id>')
def deleteUser(id):
  User.delete_user(id)
  
  return redirect("/")
  
#* =================== EDIT USER =======================

#* SHOW FORM (VIEW)

@app.route('/user/edit/<int:id>')
def edit_user_form(id):
  return render_template("edit.html", id=id)

@app.route('/user/edit', methods=["POST"])
def edit_user_data():
  User.edit_user(request.form)
  
  return redirect("/")
  
#* ============== RUN APP ================
if __name__=="__main__":   
    app.run(debug=True) 