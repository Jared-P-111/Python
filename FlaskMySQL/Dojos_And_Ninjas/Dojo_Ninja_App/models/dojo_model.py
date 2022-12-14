from Dojo_Ninja_App.config.my_sql_connection import connectToMySQL
from Dojo_Ninja_App import DATABASE
from Dojo_Ninja_App.models.ninja_model import Ninja

class Dojo:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.ninjas = []
    
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
    
    results = connectToMySQL(DATABASE).query_db(query, id)
    
    dojo = cls(results[0])
    
    for row_from_db in results: 
      ninja_data = {
        "id" : row_from_db["ninjas.id"],
        "first_name" : row_from_db["first_name"],
        "last_name": row_from_db["last_name"],
        "age": row_from_db["age"],
        "created_at": row_from_db["ninjas.created_at"],
        "updated_at" : row_from_db["ninjas.updated_at"],
        "dojo_id" : row_from_db["dojo_id"]
      }
      
      dojo.ninjas.append( Ninja(ninja_data) )
      
      print("DOJO'S NINJAS (dojo.ninjas[0]) =========>", dojo.ninjas)
    
    return dojo
