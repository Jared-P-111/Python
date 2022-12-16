import sys
sys.dont_write_bytecode = True
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app import app

bcrypt = Bcrypt(app)

#🧈 =============== HOME INDEX ROUTE ==============
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/celebrate')
def celebrate():
  return render_template("celebrate.html")

#🧈 ============ LOGIN ROUTE ===============
@app.route('/login', methods=["POST"])
def login():
  formData = { **request.form }
  
  isValid = User.validate_login(formData)
  
  if not isValid:
    return redirect('/')
  
  return redirect('/celebrate')

#🧈 ============ LOGOUT ROUTE ==============
@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

#🧈 ============ REGISTER ROUTE ============
@app.route('/register', methods=["POST"])
def register():
  formData = { **request.form }

  validated = User.validate_register(formData)

  if not validated:
    return redirect('/')
  
  User.save_user(formData)
  
  
  session["uid"] = User.save_user(formData)
  print("REGISTER FORM DATA ============>> ", formData)
  return redirect('/celebrate')