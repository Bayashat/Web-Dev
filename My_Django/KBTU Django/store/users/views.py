from django.shortcuts import render, HttpResponseRedirect

from users.models import User
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm

from django.contrib import auth

from django.urls import reverse

from storeProducts.models import Basket

from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('store:products'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data = request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    # методы для корзины 
    total_sum = 0
    total_quantity = 0
    for basket in baskets:
        total_sum += basket.sum()
        total_quantity += basket.quantity

    context = {
        "title": "Store - Профиль", 
        'form': form,
        'baskets': baskets,
        'total_sum': total_sum,
        'total_quantity': total_quantity
    }
    return render(request, 'users/profile.html', context)

