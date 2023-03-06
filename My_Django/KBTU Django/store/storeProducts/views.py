from django.shortcuts import render, HttpResponseRedirect

from .models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'title': 'storeApp',
        'username': 'Bayashat Tokmukamet',
        'is_promotion': False
    }
    return render(request, 'storeProducts/index.html', context)


def products(request):
    context = {
        'title': 'storeApp',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'storeProducts/products.html', context)


def products_new(request):
    context = {
        'title': 'products',
        'data': {
            'name': 'Bayashat',
            'University': 'KBTU',
            'Speciality': "Computer System and Software"
        }
    }
    return render(request, 'storeProducts/products_new.html', context['data'])


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=product.quantity)
    else:
        basket = baskets.first()
        basket.quantity += product.quantity
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])