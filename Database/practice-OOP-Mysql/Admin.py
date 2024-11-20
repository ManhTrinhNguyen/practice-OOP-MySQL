from Database import DB 

class Admin:
  def __init__(self, db):
    self.db = db 

  def add_book(self, title, author, genre):
    # Check if book exist 
    select_query = 'SELECT * FROM Books WHERE title = %s AND author = %s AND genre = %s'
    self.db.cursor.execute(select_query, (title, author, genre))
    book = self.db.cursor.fetchone()
    if book: 
      print('This Book is already in the Library')
      return 
    
    # Add Book if this book not exist
    query = 'INSERT INTO Books (title, author, genre) VALUES (%s, %s, %s)'
    self.db.cursor.execute(query, (title, author, genre))
    self.db.db.commit()
    print(f'Added Book {title} by {author}')

  def remove_book(self, book_id):
    # Check if book exist
    query_select = 'SELECT * FROM Books WHERE book_id = %s'
    self.db.cursor.execute(query_select, (book_id,))
    book = self.db.cursor.fetchone()
    if not book:
      print('This book is not exist!!')
      return 
    
    query = 'DELETE FROM Books WHERE book_id=%s'
    self.db.cursor.execute(query, (book_id,))
    self.db.db.commit()
    print('Deleted')

  def activate_user(self, user_id):
    # Check if user exist 
    query_select = 'SELECT * FROM Users WHERE user_id=%s'
    self.db.cursor.execute(query_select, (user_id,))
    user = self.db.cursor.fetchone()
    if not user:
      print('This user is not exist!!')
      return 
    
    if (user[3]) == 'inactive':
      query_update = 'UPDATE Users SET membership_status=%s WHERE user_id=%s'
      self.db.cursor.execute(query_update, ('active', user_id))
      print('Activated !!!')
    else:
      print('User is already Activated!!')
    
    self.db.db.commit()
    
  def deactivate_user(self, user_id):
    # Check if user exist 
    query_select = 'SELECT * FROM Users WHERE user_id=%s'
    self.db.cursor.execute(query_select, (user_id,))
    user = self.db.cursor.fetchone()
    if not user:
      print('This user is not exist!!')
      return
    
    if (user[3]) == 'active':
      query_update = 'UPDATE Users SET membership_status=%s WHERE user_id=%s'
      self.db.cursor.execute(query_update, ('inactive', user_id))
      print('Deactivated !!!')
    else:
      print('User is already Deactivated!!')
    
    self.db.db.commit()

  def view_borrowed_book(self):
    query = '''
    SELECT transaction_id, Users.name, Books.title, borrow_date, return_date
    FROM Transactions
    JOIN Users ON Transactions.user_id = Users.user_id
    JOIN Books ON Transactions.book_id = Books.book_id
    WHERE return_date IS NULL  
    '''
    self.db.cursor.execute(query)
    borrowed_books = self.db.cursor.fetchall()
    if not borrowed_books:
      print("No borrowed books found.")
      return
        
    print("Borrowed Books:")
    for book in borrowed_books:
        print(book)

    

admin1 = Admin(DB())
admin1.view_borrowed_book()

