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
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.conf.urls import handler404, handler500

#from django.conf.urls import url
from . import views

handler404 = 'views.handler404'

urlpatterns = [
    path('navbar/', TemplateView.as_view(template_name="base.html")),
    #url(r'^$',views.home),
    #url('visual', views.visual),
    #url('about', views.about)
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('visual/', TemplateView.as_view(template_name="visual.html"), name="visual"),
    path('bydept/', TemplateView.as_view(template_name="by_dept.html"), name="bydept"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('categories/', views.CategoryListView.as_view(), name="category-list"),
    path('categories/<str:category_name>/', views.CategoryListView.as_view(), name="category-list-single"),
    path('customers/', views.CustomerListView.as_view(), name="customer-list"),
    path('categories/<str:occupation_name>/', views.CustomerListView.as_view(), name="customer-list-single"),

    # TODO: refreshing following page jumps to bottom of category page.
    # path('categories/<slug:category-slug>/', RedirectView.as_view(url='categories/'), name="category-list"),

    #currently this is never being called
    path('categories/<slug:category>/<slug:product>/', views.ProductDetailView.as_view(), name="product-detail"),
    path('purchase/', TemplateView.as_view(template_name="purchase.html"), name="purchase"),


]
