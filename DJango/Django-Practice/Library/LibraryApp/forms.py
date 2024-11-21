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

  # Exclude book already borrow by overiding the queryset
  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args, **kwargs)
  #   self.fields['book'].queryset = BookModel.objects.filter(is_available = True)

