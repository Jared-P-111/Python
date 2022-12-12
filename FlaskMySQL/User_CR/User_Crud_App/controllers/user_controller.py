from flask import Flask, render_template, request, redirect, session
from User_Crud_App.models.user_model import User
from User_Crud_App import app


#* ================= HOME VIEW ==================
@app.route('/')
def readAll():
  currUsers = User.get_all()
  return render_template("readAll.html", currUsers=currUsers)

#* ================ ONE USER VIEW ===============

@app.route('/user/<int:id>')
def getUser(id):
  user = User.get_one_user(id)
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
  newUserData = {**request.form}
  #* PASS DICTIONARY FROM request.form TO CLASS METHOD create_user
  newUser = User.create_user(newUserData)
  user = User.get_one_user(newUser)
  
  return render_template("readOne.html", user=user)

#* =================== DELETE USER ======================

@app.route('/delete/<int:id>')
def deleteUser(id):
  User.delete_user(id)
  
  return redirect("/")
  
#* =================== EDIT USER =======================

#* SHOW FORM (VIEW)

@app.route('/user/edit/<int:id>')
def edit_user_form(id):
  user = User.get_one_user(id)
  print(user)
  return render_template("edit.html", id=id, user=user)

@app.route('/user/edit', methods=["POST"])
def edit_user_data():
  User.edit_user(request.form)
  
  return redirect("/")