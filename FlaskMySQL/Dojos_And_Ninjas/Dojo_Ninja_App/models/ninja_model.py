from Dojo_Ninja_App.config.my_sql_connection import connectToMySQL
from Dojo_Ninja_App import DATABASE

class Ninja:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.age = data['age']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    
  @classmethod
  def get_all_ninjas(cls):
    ninjas = []
    query = "SELECT * FROM ninjas;"
    results = connectToMySQL(DATABASE).query_db(query)
    
    if results:
      for ninja in results:
        this_ninja = cls(ninja)
        ninjas.append(this_ninja)
        
    return ninjas
  
  @classmethod
  def create_new(cls, data):
    query = """
      UPDATE users SET 
        first_name = %(first_name)s, 
        last_name = %(last_name)s,
        email = %(email)s
      WHERE id = %(id)s
    """
    newNinja = connectToMySQL(DATABASE).query_db(query, data)
    return newNinja
    