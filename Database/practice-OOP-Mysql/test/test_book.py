from unittest import TestCase
from unittest.mock import MagicMock, patch

import sys 

sys.path.insert(1, "/Users/trinhnguyen/Documents/Meta-Certificate/Database/practice-OOP-Mysql/")
from Database import DB
from Book import Book

class TestBook(TestCase):
  @patch("mysql.connector.connect") # Pass mock mysql.connector.connect as arg
  def setUp(self, mock_connect): # Set up method run at the beginning of each test
    # Mock connect db
    self.mock_db = MagicMock()
    # Mock cursor
    self.mock_cursor = MagicMock()
    
    # Mock connect will return value as mock_db
    mock_connect.return_value = self.mock_db 

    # Mock_db.cursor will return value self.mock_cursor 
    self.mock_db.cursor.return_value = self.mock_cursor

    # Initialize DB 
    self.book = Book(DB(), 'Rich Dad Poor Dad', 'Robert Kiosaki', 'Money')

  def test_add_book(self):
    # Call method want to test
    self.book.add_book()

    # Query insert 
    query = 'INSERT INTO Books (title, author, genre) VALUES (%s, %s, %s)'
    self.mock_cursor.execute.assert_any_call(
      query,
      ('Rich Dad Poor Dad', 'Robert Kiosaki', 'Money')
    )
    # Commit 
    self.mock_db.commit.assert_called_once()
  
  def test_search_book(self):
    # Call method want to test
    self.book.search_book(1)

    # Query select
    query = 'SELECT * FROM Books Where book_id = %s'

    self.mock_cursor.execute.assert_any_call(
      query,
      (1,)
    )

  def test_remove_book(self):
    # Call method want to test
    self.book.remove_book(1)

    # Query Delete
    query_delete = 'DELETE FROM Books WHERE book_id = %s'

    self.mock_cursor.execute.assert_any_call(
      query_delete,
      (1,)
    )
    # Commit 
    self.mock_db.commit.assert_called_once()

