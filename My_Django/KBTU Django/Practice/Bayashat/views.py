from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'name': 'Bayashat'}
    return render(request, 'index.html')