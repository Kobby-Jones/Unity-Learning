from django.shortcuts import render,  redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Crete the homepage
def index(request):
    return render(request, 'users/_base.html')

# Crete the registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
         form = UserCreationForm()
    return render(request, 'registation/register.html')

def test(request):
    return render(request, )