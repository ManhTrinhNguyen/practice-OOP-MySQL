REATE DATABASE LibraryDB;
USE LibraryDB;

-- Users Table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    membership_status ENUM('active', 'inactive') DEFAULT 'active'
);

-- Books Table
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100),
    genre VARCHAR(50),
    availability_status ENUM('available', 'borrowed') DEFAULT 'available'
);

-- Transactions Table
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
2. Python Class Design
We’ll use OOP principles to define three main classes: User, Book, and Library.

Basic Class Structure
python
Copy code
import mysql.connector
from datetime import date

# Database Connection Class
class Database:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

# User Class
class User:
    def __init__(self, db, user_id=None, name=None, email=None):
        self.db = db
        self.user_id = user_id
        self.name = name
        self.email = email

    def register(self):
        query = "INSERT INTO Users (name, email) VALUES (%s, %s)"
        self.db.execute(query, (self.name, self.email))
        print(f"User {self.name} registered successfully.")

    def get_user_details(self):
        query = "SELECT * FROM Users WHERE user_id = %s"
        return self.db.fetchone(query, (self.user_id,))

# Book Class
class Book:
    def __init__(self, db, book_id=None, title=None, author=None, genre=None):
        self.db = db
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

    def add_book(self):
        query = "INSERT INTO Books (title, author, genre) VALUES (%s, %s, %s)"
        self.db.execute(query, (self.title, self.author, self.genre))
        print(f"Book '{self.title}' added to the library.")

    def search_books(self, keyword):
        query = "SELECT * FROM Books WHERE title LIKE %s OR author LIKE %s OR genre LIKE %s"
        return self.db.fetchall(query, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

# Library Class
class Library:
    def __init__(self, db):
        self.db = db

    def borrow_book(self, user_id, book_id):
        # Check availability
        book_query = "SELECT availability_status FROM Books WHERE book_id = %s"
        book = self.db.fetchone(book_query, (book_id,))
        if not book or book['availability_status'] == 'borrowed':
            print("Book is not available for borrowing.")
            return

        # Borrow book
        transaction_query = "INSERT INTO Transactions (user_id, book_id) VALUES (%s, %s)"
        update_book_query = "UPDATE Books SET availability_status = 'borrowed' WHERE book_id = %s"
        self.db.execute(transaction_query, (user_id, book_id))
        self.db.execute(update_book_query, (book_id,))
        print(f"Book {book_id} borrowed successfully.")

    def return_book(self, user_id, book_id):
        # Return book
        return_query = "UPDATE Transactions SET return_date = %s WHERE user_id = %s AND book_id = %s AND return_date IS NULL"
        update_book_query = "UPDATE Books SET availability_status = 'available' WHERE book_id = %s"
        self.db.execute(return_query, (date.today(), user_id, book_id))
        self.db.execute(update_book_query, (book_id,))
        print(f"Book {book_id} returned successfully.")
