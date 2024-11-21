from django.urls import path
from . import views 

urlpatterns = [
  path('', views.list_books, name='books'),
  path('users/', views.list_users, name='users'),
  path('user/<int:pk>', views.user_detail, name='user'),

  path('book/<int:pk>', views.book_detail, name='book'),
  path('add-book', views.add_book, name = 'add-book'),
  path('update-book/<int:pk>', views.update_book, name='update'),
  path('delete-book/<int:pk>', views.delete_book, name='delete_book'),

  path('borrow-book', views.borrow_book, name ='borrow'),
  path('return-book/<int:pk>', views.return_borrow_book, name ='return'), 
  path('borrow-list', views.list_borrower, name='borrow-list'),
]