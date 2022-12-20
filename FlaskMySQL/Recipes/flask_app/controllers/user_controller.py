import sys
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app import app

bcrypt = Bcrypt(app)

#🧈=========== Prevent __pycache files ==============
sys.dont_write_bytecode = True


#🧈 ========== INDEX ==============
@app.route('/')
def index():
  return render_template("index.html")
  

#🧈 ============ LOGIN ===============
@app.route('/login', methods=["POST"])
def login():
  formData = { **request.form } 
  
  isValid = User.validate_login(formData)
  
  if not isValid:
    return redirect('/')
  
  user_data = {'email': request.form['email']}
  this_user = User.get_one_user(user_data)
  session['uid'] = this_user.id
  
  return redirect('/recipes')

#🧈 ============ REGISTER ============
@app.route('/register', methods=["POST"])
def register():
  formData = { **request.form } 

  validated = User.validate_register(formData)

  if not validated:
    return redirect('/')
  
  session["uid"] = User.save_user(formData)
  return redirect('/recipes')

#🧈 ============ LOGOUT ==============
@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')