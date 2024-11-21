from django.shortcuts import render, get_object_or_404, redirect
from .models import UserModel, BookModel, TransactionModel
from .forms import UserModelForm, BookModelForm, TransactionModelForm
from django.contrib import messages

# Create your views here.

###### BOOK #####
def list_books(request):
  books = BookModel.objects.all()
  return render(request, 'books.html', {'books': books})

def book_detail(request, pk):
  book = get_object_or_404(BookModel, pk = pk)
  return render(request, 'book.html', {'book': book})

def add_book(request):
  form = BookModelForm()
  if request.method == 'POST':
    form = BookModelForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('books')
    
  return render(request, 'form.html', {'form': form})

def update_book(request, pk):
  book = get_object_or_404(BookModel, pk=pk)
  form = BookModelForm(instance=book)

  if request.method == 'POST':
    form = BookModelForm(request.POST, instance=book)
    if form.is_valid():
      form.save()
      return redirect('books')
  
  return render(request, 'form.html', {'form': form})

def delete_book(request, pk):
  book = get_object_or_404(BookModel, pk=pk)
  if request.method == 'POST':
    book.delete()
    return redirect('books')
  return render(request, 'delete_book.html', {'book': book})

    ######################

############ USER ############
def list_users(request):
  users = UserModel.objects.all()
  return render(request, 'users.html', {'users': users})

def user_detail(request, pk):
  user = get_object_or_404(UserModel, pk=pk)
  return render(request, 'user.html', {'user': user})

#######################

 ############## BORROW RETURN ##########
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
        return redirect('books')
      
      # Update available status 
      book.is_available = False 
      book.save()

      # Save Transaction 
      transaction.save()

      messages.success(request, f"You have borrowed {book.title}")
      return redirect('books')
  
  return render(request, 'form.html', {'form': form})

# Return Book
def return_borrow_book(request, pk):
  # Get transaction by its Id
  transaction = get_object_or_404(TransactionModel, pk=pk)

  # Check if return yet ? 
  if transaction.return_date:
    messages.error(request, 'Book already returned')
    return redirect('books')
   
  form = TransactionModelForm(instance=transaction)
  if request.method == 'POST':
    form = TransactionModelForm(request.POST, instance=transaction)
    if form.is_valid():
      transaction_form = form.save(commit=False)
      # Get Book by transaction Id
      book = get_object_or_404(BookModel, id=transaction_form.book.id)

      # Check if book status is True 
      if book.is_available == True: 
        messages.error(request, f'This {book.title} is not borrwed yet')
        return redirect('books')

      # Update book status
      book.is_available = True

      # Save book and tranasction form
      book.save() 
      transaction_form.save()

      messages.success(request, f'You have returned {book.title}')

      return redirect('books')
  return render(request, 'form.html', {'form': form})


# Borrower List 
def list_borrower(request):
  transactions = TransactionModel.objects.all()
  return render(request, 'borrow_list.html', {'transactions': transactions})
#######################

