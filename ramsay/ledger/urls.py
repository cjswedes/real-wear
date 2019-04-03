"""spike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

#from django.conf.urls import url
from . import views

urlpatterns = [
    # url('navbar', view.navbar),
    #url(r'^$',views.home),
    #url('visual', views.visual),
    #url('about', views.about)
    path('', TemplateView.as_view(template_name="home.html")),
    path('visual/', TemplateView.as_view(template_name="visual.html")),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('categories/', views.CategoryListView.as_view(), name="category-list"),
    # TODO: refreshing following page jumps to bottom of category page.
    # path('categories/<slug:category>/', RedirectView.as_view(url='categories/'), name="category-list"),
    path('categories/<slug:category>/<slug:product>/', views.ProductDetailView.as_view(), name="product-detail"),
    path('customers/', views.CustomerListView.as_view(), name="customer-list")

]
