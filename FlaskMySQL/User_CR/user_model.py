from my_sql_connection import connectToMySQL


class User:
  def __init__( self , data ):
      self.id = data['id']
      self.first_name = data['first_name']
      self.last_name = data['last_name']
      self.email = data['email']
        

#* ============== READ ALL USERS =================

  @classmethod
  def get_all(cls):
      users = []      
      query = "SELECT * FROM users;"
      results = connectToMySQL('users').query_db(query)

      if results:
        for user in results:
          this_user = cls(user)
          users.append(this_user)
          
      return users
    
#* ============== CREATE NEW USER =============
    
  @classmethod
  def create_user(cls, data):
    query = """
      INSERT INTO users (first_name, last_name, email) 
      VALUES ("%(first_name)s", "%(last_name)s", "%(email)s")
    """
    
    
    return connectToMySQL('users').query_db(query, data)
  
#* ==============  ====================