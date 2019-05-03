from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.urls import reverse_lazy
from django.views import generic
from .models import Category, Product, Customer
from random import randint
'''
# All in Class Based View already
def navbar(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def visual(request):
    return render(request, 'visual.html')

def about(request):
    return render(request, 'about.html')

def search(request):
    return render(request, 'search_results.html')    
'''
def handler404(request, exception):
    message = ["Whoops we must have misplaced this tutorial, please use the search bar above.",
                "Darn we did it again we put the tutorial is the wrong place sorry, use that sweet search bar above",
                "What tutorial are you looking for? Tell us in the search bar above."
                ]
    context = {
        'message': message[randint(0,2)]
    }
    return render(request, "404.html", context, status=404)
    
class CategoryListView(generic.ListView):
    model        = Category
    paginate_by  = 5  # 5 for testing, TODO: 20? 
    template_name= 'category_list.html'

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search', None)
        if search:
            selected = None
            #search query
            products = Product.objects.filter(title__icontains=search).only('title_slug', 'title', 'materials', 'dimensions',
                                                'production_city', 'original_price', 'modern_dollars')

        else:
            if 'category_name' in kwargs.keys():
                selected = kwargs['category_name']
                products = Product.objects.filter(category=kwargs['category_name'])\
                                          .only('title_slug', 'title', 'materials', 'dimensions',
                                                'production_city', 'original_price', 'modern_dollars')
            else:
                selected = None
                products = Product.objects.all()\
                                          .only('title_slug', 'title', 'materials', 'dimensions',
                                                'production_city', 'original_price', 'modern_dollars')
        categories = Category.objects.all().only('name', 'name_slug')
        return render(request, 'category_list.html', {'categories': categories, 'products': products, 'selected': selected})

class ProductDetailView(generic.DetailView):
    model=Product
    template_name = 'product_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(title_slug=kwargs['product'])
        except:
            return render(request, self.template_name, {'product': None})
        return render(request, self.template_name, {'product': product})

class CustomerListView(generic.ListView):
    model       = Customer
    paginate_by = 10
    template_name = 'customer_list.html'

    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        if 'occupation_name' in kwargs.keys():
            selected = kwargs['occupation_name']
            occupations = Customer.objects.filter(occupation=kwargs['occupation_name']).distinct('occupation')\
                                        .only('first_name', 'last_name', 'occupation')
        else:
            selected = None
            occupations = Customer.objects.distinct('occupation')\
                                        .only('first_name', 'last_name', 'occupation')
        
        return render(request, 'customer_list.html', {'customers' : customers, 'occupations': occupations})