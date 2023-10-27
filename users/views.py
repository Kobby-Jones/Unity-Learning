from django.shortcuts import render,  redirect
from .forms import UserForm
from django.urls import reverse


# Crete the homepage
def index(request):
    return render(request, 'users/_base.html')

# Crete the registration view
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
         form = UserForm()

    return render(request, 'users/register.html', {'form':form})
