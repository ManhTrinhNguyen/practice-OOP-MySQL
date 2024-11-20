from django import forms 
from .models import UserModel, BookModel, TransactionModel

class UserModelForm(forms.ModelForm):
  class Meta:
    model = UserModel 
    fields = '__all__'

class BookModelForm(forms.ModelForm):
  class Meta:
    model = BookModel 
    fields = '__all__'

class TransactionModelForm(forms.ModelForm):
  class Meta:
    model = TransactionModel
    fields = '__all__'

