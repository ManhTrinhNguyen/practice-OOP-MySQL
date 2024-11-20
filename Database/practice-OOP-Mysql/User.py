from Database import DB 

class User: 
  def __init__(self,db ,name, email):
    self.name = name
    self.email = email 
    self.db = db 

  def register(self):
    query = 'INSERT INTO Users (name, email) VALUES (%s, %s)'
    self.db.cursor.execute(query, (self.name, self.email))
    self.db.db.commit()
    print(f'User {self.name} successfully registered')

  def get_user_detail(self, user_id):
    query = 'SELECT * FROM Users WHERE user_id=%s'
    self.db.cursor.excute(query, (user_id,))
    return self.db.cursor.fetchone()
  

