from Dojo_Ninja_App.config.my_sql_connection import connectToMySQL
from Dojo_Ninja_App import DATABASE

class Dojo:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    
#* =============== GET ALL DOJOS =================
  @classmethod
  def get_all_dojos(cls):
    dojos = []
    query = "SELECT * FROM dojos;"
    results = connectToMySQL(DATABASE).query_db(query)
    
    if results:
      for dojo in results:
        this_dojo = cls(dojo)
        dojos.append(this_dojo)
        
    return dojos
  
#* =============== GET ONE DOJO =================
  @classmethod
  def get_one_dojo(cls, id):
    query = """SELECT * FROM dojos WHERE id = %(id)s"""
    dojoId = { "id" : id }
    
    dojo = connectToMySQL(DATABASE).query_db(query, dojoId)

    return dojo
  
  
#* ================ CREATE NEW ================

  @classmethod
  def create_new(cls, data):
    query = """
      INSERT INTO dojos (name) VALUES (%(name)s);
    """
    newDojo = connectToMySQL(DATABASE).query_db(query, data)
    return newDojo
  
#* ========= GET ALL NINJAS FROM A DOJO ============
  @classmethod
  def get_all_ninjas_from_dojo(cls, id):
    query = """
      SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
      WHERE dojos.id = %(id)s;
    """
    
    currDojoNinjas = connectToMySQL(DATABASE).query_db(query, id)
    return currDojoNinjas
