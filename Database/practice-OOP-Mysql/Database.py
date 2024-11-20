import mysql.connector 
from dotenv import load_dotenv 
load_dotenv()
import os 

class DB:
  def __init__(self):
    self.db = mysql.connector.connect(
      host='localhost',
      user=os.getenv('DB_USER'),
      password=os.getenv('DB_PASSWORD'),
      database='library_practice_3'
    )
    self.cursor = self.db.cursor()

