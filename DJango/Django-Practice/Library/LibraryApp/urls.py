from django.urls import path
from . import views 

urlpatterns = [
  path('', views.list_books, name='books'),
  path('users/', views.list_users, name='users'),
  path('book/<int:pk>', views.book_detail, name='book'),
  path('user/<int:pk>', views.user_detail, name='user'),
  path('borrow-book', views.borrow_book, name ='borrow'),
]