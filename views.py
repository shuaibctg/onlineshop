from django.shortcuts import render
from .models import Product
from math import ceil


# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    print(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    allProds = [[products, range(1, nSlides,), nSlides],
                [products, range(1, nSlides,), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)
    # params = {'no_of_slides': nSlides, 'range': range(nSlides), 'product': products, }



def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def productView(request):
    return render(request, 'shop/products.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
