import sys
sys.dont_write_bytecode = True
import pprint

from flask import render_template, redirect, request
from flask_app.models.user_model import User
from flask_app import app


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
  formData = { **request.form }
  print("LOGIN FORM DATA ===========>> ", formData)
  return redirect('/')

@app.route('/register', methods=["POST"])
def register():
  formData = { **request.form }
  print("REGISTER FORM DATA ============>> ", formData)
  return redirect('/')