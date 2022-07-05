from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']