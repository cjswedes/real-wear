from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from .models import Category, Product, Customer
def navbar(request):
    context = {}
    # context['hello'] = 'hello world!'
    # return HttpResponse("Hello world!")
    return render(request, 'base.html', context)

def home(request):
    return render(request, 'home.html')

def visual(request):
    return render(request, 'visual.html')

def about(request):
    return render(request, 'about.html')


class CategoryListView(generic.ListView):
    model        = Category
    paginate_by  = 10
    template_name= 'category_list.html'

    def get(self, request, *args, **kwargs):
        if 'category_name' in kwargs.keys():
            selected = kwargs['category_name']
            products = Product.objects.filter(category=kwargs['category_name'])\
                                      .only('title_slug', 'title', 'materials', 'dimensions',
                                            'origin', 'original_price', 'modern_dollars')
        else:
            selected = None
            products = Product.objects.all()\
                                      .only('title_slug', 'title', 'materials', 'dimensions',
                                            'origin', 'original_price', 'modern_dollars')
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
        return render(request, 'customer_list.html', {'customers' : customers})
