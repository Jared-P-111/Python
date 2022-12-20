from flask import flash, session
from flask_app import DATABASE, app
from flask_app.config.my_sql_connection import connectToMySQL
from flask_app.models.user_model import User



class Recipe:
  def __init__(self, data):
    self.id = data['id']
    self.posted_by_user_id = data['posted_by_user_id']
    self.recipe_name = data['recipe_name']
    self.description = data['description']
    self.instructions = data['instructions']
    self.date_cooked = data['date_cooked']
    self.under_30_min = data['under_30_min']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

#🧈=============== GET ONE RECIPE =================
  @classmethod
  def get_one_recipe(cls, id):
    query = """
      SELECT * FROM recipes WHERE id = %(id)s;
    """
    results = connectToMySQL(DATABASE).query_db(query, id)
    print(f"get_one_recipe --> id: {id} : {query} \n\n {results}")
    return results
  
#🧈 ============== CREATE RECIPE ==================
  @classmethod
  def create_recipe(cls, data):
    query = """
      INSERT INTO recipes (posted_by_user_id, recipe_name, description, instructions, date_cooked, under_30_min) 
      VALUES (%(posted_by_user_id)s, %(recipe_name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30_min)s);
    """
    results = connectToMySQL(DATABASE).query_db(query, data)
    return results

#🧈================= GET ALL RECIPES BY USER ===================
  @classmethod
  def get_all_recipes_by_user(cls, input):
    query = """
      SELECT * FROM recipes WHERE posted_by_user_id = %(id)s
    """
    results = connectToMySQL(DATABASE).query_db(query, input)
    return results
  
#🧈=================== GET ALL USERS AND RECIPES ==================
  @classmethod
  def get_all_users_and_recipes(cls):
    query = """
      SELECT * FROM recipes JOIN users ON recipes.posted_by_user_id = users.id
    """
    results = connectToMySQL(DATABASE).query_db(query)
    
    all_recipes =  []
    
    #🧈 ========= GET DATA AND INSTANTIATE RECIPES INTO LIST =========
    for row in results:
      recipe = cls(row) #🧈<-- Instantiated class recipe()
      
      """
        Because we got two tables of data from the join query we have to disambiguate the 
        data. We do this by reassigning the names to not be .dot notation connected thus 
        making this a new user_data object that can be used to instantiate a User into the 
        recipe instance. So we are making a recipe instance and a new user instance inside of it. 
    """
      
      user_data = { #🧈<-- clean data from query for new recipe data, disambiguate
        **row, 
        "id": row["users.id"],
        "updated_at": row["users.updated_at"],
        "created_at": row["users.created_at"],
      }
      
      recipe.created_by = User(user_data) #🧈<-- Instantiate User() with new data into recipe.
      all_recipes.append(recipe)
      
    return all_recipes
  
  