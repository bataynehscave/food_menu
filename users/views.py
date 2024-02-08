from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm
# Create your views here.
def create(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'you have succefully logged in {username} welcome!')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')