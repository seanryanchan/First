from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('about', views.aboutUs, name='about'),
    path('business', views.businessWithUs, name='business'),
    path('contact', views.contact, name='contact')
]
