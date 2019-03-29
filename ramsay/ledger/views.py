from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from .models import Category, Product
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
        categories = Category.objects.all()
        return render(request, 'category_list.html', {'categories':categories})
class ProductDetailView(generic.DetailView):
    model=Product
    template_name = 'product_detail.html'
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(slug=kwargs['product'])
        return render(request, self.template_name, {'product': product})
