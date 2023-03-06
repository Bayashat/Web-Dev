from django.shortcuts import render, HttpResponseRedirect

from users.models import CustomUser
from .forms import CustomUserLoginForm

from django.contrib import auth

from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data = request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse(''))
    else:
        form = CustomUserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)