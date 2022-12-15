from flask import flash
import sys
sys.dont_write_bytecode = True

class User:
  def __init__(self, data):
    self.id = data['id']
    self.email = data['email']
    self.username = data['username']
    self.password = data['password']
    self.created_at = data['create_at']
    self.updated_at = data['updated_at']
    
  @staticmethod
  def validate_login(input):
      is_valid = True
      
      if len(input['name']) < 3:
          flash("Name must be at least 3 characters.")
          is_valid = False
          
      return is_valid