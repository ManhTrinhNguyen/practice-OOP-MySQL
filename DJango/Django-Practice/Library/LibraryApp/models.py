from django.db import models

# Create your models here.
class UserModel(models.Model):
  STATUS_CHOICE = (
    ('active', 'Active'),
    ('inactive', 'Inactive')
  )

  name = models.CharField(max_length=250)
  email = models.EmailField()
  memebership_status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='active')

  def __str__(self):
    return self.name 
  

class BookModel(models.Model):
  title = models.CharField(max_length=250)
  author = models.CharField(max_length=250)
  genre = models.CharField(max_length=100)
  is_available = models.BooleanField(default=True)

  def __str__(self):
    return self.title


class TransactionModel(models.Model):
  borrow_date = models.DateField(auto_now_add=True)
  return_date = models.DateField(blank=True, null=True)
  user = models.ForeignKey(UserModel, on_delete=models.CASCADE) # Link to user model 
  book = models.ForeignKey(BookModel, on_delete=models.CASCADE) # Link to book model 

  def __str__(self):
    return f'{self.user.name} borrowed {self.book.title}'



