from django.shortcuts import render, get_object_or_404, redirect
from .models import UserModel, BookModel 
from .forms import UserModelForm, BookModelForm, TransactionModelForm
from django.contrib import messages

# Create your views here.
def list_books(request):
  books = BookModel.objects.all()
  return render(request, 'books.html', {'books': books})

def list_users(request):
  users = UserModel.objects.all()
  return render(request, 'users.html', {'users': users})

def book_detail(request, pk):
  book = get_object_or_404(BookModel, pk = pk)
  return render(request, 'book.html', {'book': book})

def user_detail(request, pk):
  user = get_object_or_404(UserModel, pk=pk)
  return render(request, 'user.html', {'user': user})

# Borrow Book 
def borrow_book (request):
  form = TransactionModelForm()
  if request.method == 'POST':
    form = TransactionModelForm(request.POST)
    if form.is_valid():
      # Save Transaction but not commit to database yet
      transaction = form.save(commit=False)

      # Check if book available 
      book = get_object_or_404(BookModel,id=transaction.book.id)
      if book.is_available == False:
        messages.error(request, f"{book.title} is already borrowed")
        redirect('books')
      
      # Update available status 
      book.is_available = False 
      book.save()

      # Save Transaction 
      transaction.save()

      messages.success(request, f"You have borrowed {book.title}")
      return redirect('books')
  
  return render(request, 'form.html', {'form': form})


