from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField

class UserForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model =  User
        fields = ['username', 'email', 'password1', 'password2']