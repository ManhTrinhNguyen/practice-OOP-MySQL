from Book import Book
from User import User
from Database import DB
from datetime import date 

class LibraryManagement:
  def __init__(self, db):
    self.db = db

  def borrow_book(self, user_id, book_id):
    # Check if Book available to borrow 
    select_query_book = 'SELECT availability_status FROM Books WHERE book_id = %s'
    self.db.cursor.execute(select_query_book, (book_id,))  
    book_status = self.db.cursor.fetchone()
    if book_status[0] == 'borrowed' or not book_status:
      print('This book is not available')
      return 
    
    # Borrow Book Transaction 
    insert_query_transaction = 'INSERT INTO Transactions (user_id, book_id) VALUES (%s, %s)'
    self.db.cursor.execute(insert_query_transaction, (user_id, book_id))

    # Update Book to borrowed 
    update_query_book = 'UPDATE Books SET availability_status = %s WHERE book_id = %s'
    self.db.cursor.execute(update_query_book, ('borrowed' ,book_id,))

    self.db.db.commit()
    print(f'Success borrowed')

  def return_book(self, user_id, book_id):
    return_query = 'UPDATE Transactions SET return_date = %s WHERE book_id=%s AND user_id=%s AND return_date IS NULL'
    update_query_book = "UPDATE Books SET availability_status = %s WHERE book_id=%s"
    self.db.cursor.execute(return_query, (date.today() ,book_id, user_id))
    self.db.cursor.execute(update_query_book, ('available' ,book_id))
    self.db.db.commit()
    print('Return Success')

    

    


library = LibraryManagement(DB())
library.borrow_book(2,2)