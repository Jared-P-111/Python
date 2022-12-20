from flask import flash, session
from flask_bcrypt import Bcrypt
from flask_app import DATABASE, app
from flask_app.config.my_sql_connection import connectToMySQL

import re
import sys
sys.dont_write_bytecode = True

bcrypt = Bcrypt(app)

class User:
  def __init__(self, data):
    self.id = data['id']
    self.email = data['email']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    
  @classmethod
  def create_user(cls, data):
    query = """
      INSERT INTO users (first_name, last_name, email) 
      VALUES (%(first_name)s, %(last_name)s, %(email)s)
    """
    return connectToMySQL('recipes_db').query_db(query, data)
  
  #🧈================ SAVE USER ===================
  @classmethod
  def save_user(cls, input):
    pw_hash = bcrypt.generate_password_hash(input["password"])
    input["password"] = pw_hash
    query = """INSERT INTO users (first_name, last_name, email, password)
    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
    user = connectToMySQL(DATABASE).query_db(query, input)
    return user 
    
  #🧈================ GET USER BY ID ==============
  @classmethod
  def get_user_by_id(cls, input):
    query = """SELECT * FROM users WHERE id = %(id)s"""
    results = connectToMySQL(DATABASE).query_db(query, input)
    print(f"RESULTS!!!!!!!!!!! {results}")
    if results: #🍔<============ CHECK IF USER IN DB
      user = cls(results[0]) #🍔<========= INSTANTIATE USER FROM DB
      return user
    else:
      return False

  #🧈================ GET ONE USER ================
  @classmethod
  def get_one_user(cls, input):
    query = """SELECT * FROM users WHERE email = %(email)s"""
    results = connectToMySQL(DATABASE).query_db(query, input)
    
    if len(results) < 1: #🍔<============ CHECK IF USER IN DB
      return False
    else:
      user = cls(results[0]) #🍔<========= INSTANTIATE USER FROM DB
      return user


#🧈============== VALIDATE LOGIN ===============
  @classmethod
  def validate_login(cls, input):
    user = cls.get_one_user(input)
    
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    is_email_valid = EMAIL_REGEX.match(input['email'])
    is_valid = True
    
    if not is_email_valid:
      flash("Invalid Inputs", "login_error")
      is_valid = False
      return is_valid
    
    if not user:
      flash("Invalid Inputs", "login_error")
      is_valid = False
      return is_valid
      
    if user: 
    #🧈Now check passwords
      if not bcrypt.check_password_hash(user.password, input["password"]):
        flash("invalid credentials - pass", "log")
        is_valid = False
        return is_valid
      
    return is_valid
  
  #🧈=============== VALIDATE REGISTRATION ==================
  @staticmethod
  def validate_register(input):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    is_email_valid = EMAIL_REGEX.match(input['email'])
    is_valid = True
    
    #🧈========== CHECK FOR LENGTH OF FIRST NAME ============
    if input['first_name'] == "" and len(input['first_name']) < 2:
      flash("First Name is not long enough", "register_error")
      is_valid = False
    
    #🧈========== CHECK FOR LENGTH OF LAST NAME =============
    if input['last_name'] == "" and len(input['last_name']) < 2:
      flash("Last name is not long enough", "register_error")
      is_valid = False
    
    #🧈========== CHECK OF EMPTY INPUT FIELD ON EMAIL =======
    if input['email'] == "":
      flash("You need to enter a valid email", "register_error")
      is_valid = False
    
    #🧈========== QUERY DB TO SEE IF EMAIL IS IN DB =========
    if input['email'] and is_email_valid:
      query = """SELECT * FROM users WHERE email = %(email)s"""
      checkForEmail = connectToMySQL(DATABASE).query_db(query, input)
      
      if len(checkForEmail) > 0:
        flash("Not valid entries", "register_error")
        is_valid = False      
      
      #🧈======== CHECK REGEX FOR VALID EMAIL ===============
      if not is_email_valid:
        flash("Not valid entries", "register_error")
        is_valid = False
    
    #🧈========== CHECK LENGTH PW AND IF IN FORM ============
    if not input['password'] or len(input['password']) < 2:
      flash("Not valid entries", "register_error")
      is_valid = False
    
    #🧈========== CHECK PW AND CONFIRM PW ===========
    if input['password'] != input['confirm_password']:
      flash("Your passwords do not match", "register_error")
      is_valid = False
      
    return is_valid