from Database import DB

class Book:
  def __init__(self, db ,title, author, genre):
    self.title = title
    self.author = author 
    self.genre = genre 
    self.db = db 

  def add_book(self):
    query = 'INSERT INTO Books (title, author, genre) VALUES (%s, %s, %s)'
    self.db.cursor.execute(query, (self.title, self.author, self.genre))
    self.db.db.commit()
    print(f'Added Book: {self.title} by Author: {self.title}')
  
  def search_book(self, book_id):
    query = 'SELECT * FROM Books Where book_id = %s'
    self.db.cursor.execute(query, (book_id,))
    return self.db.cursor.fetchone()
  
  def remove_book(self, book_id):
    query = 'DELETE FROM Books WHERE book_id = %s'
    self.db.cursor.execute(query, (book_id, ))
    self.db.db.commit()
    print('Deleted')

# book1 = Book(DB(), '7 Highly Effective People', 'Steve', 'Self Improving')

# book1.add_book()