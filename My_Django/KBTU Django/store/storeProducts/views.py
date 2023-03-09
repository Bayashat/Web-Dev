from django.shortcuts import render, HttpResponseRedirect

from .models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required

# import Pagination Stuff
from django.core.paginator import Paginator

def index(request):
    context = {
        'title': 'storeApp',
        'username': 'Bayashat Tokmukamet',
        'is_promotion': False
    }
    return render(request, 'storeProducts/index.html', context)


def products(request, category_id=None):
    # Set up Pagination
    objects = ProductCategory.objects.all()
    p = Paginator(objects, 2)  # first-what objects you want to paginate, second-how many page you want show in one page
    
    page_number =  request.GET.get('page')
    category_obj = p.get_page(page_number)

    # print(p.count)  # number of objects 
    # print(p.num_pages)  # number of pages : p.count / 2
    # print(p.page_range)  # range(1, 2)

    if category_id:
        category = ProductCategory.objects.get(id = category_id)
        products = Product.objects.filter(category = category)
    else:
        products = Product.objects.filter(category = category_obj[0])  # Only shows the first obj in category_obj(Shoes)


    context = {
        'title': 'storeApp',
        'products': products,
        'categories': ProductCategory.objects.all(),
        'category_obj': category_obj,
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

@login_required
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

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

