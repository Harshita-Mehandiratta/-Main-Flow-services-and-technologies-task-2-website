#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#authentication code
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]


# In[ ]:


#models details code
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


# In[ ]:


#product details code
<!-- Example HTML template for product detail -->
{% extends "base.html" %}

{% block content %}
  <h1>{{ product.name }}</h1>
  <p>Description: {{ product.description }}</p>
  <p>Price: ${{ product.price }}</p>
{% endblock %}


# In[ ]:


#product list code
<!-- Example HTML template for product list -->
{% extends "base.html" %}

{% block content %}
  <h1>Product List</h1>
  <ul>
    {% for product in products %}
      <li>
        <a href="{% url 'product_detail' product.id %}">{{ product.name }}</a> - ${{ product.price }}
      </li>
    {% endfor %}
  </ul>
{% endblock %}


# In[ ]:


#store details code
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


# In[ ]:


#urls code
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # Add cart-related URLs here.
]

