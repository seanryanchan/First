from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from Write_ups.models import Write_up
from Products.models import Product

from django.db import DataError

def index(request):
    vision_mission = get_object_or_404(Write_up, id_name="vision_mission")
    history = get_object_or_404(Write_up, id_name="history")
    context = {
        'vision_mission': vision_mission,
        'history': history,
    }
    return render(request, 'Pages/index.html', context)

def products(request):
    try:
        product_list = Product.objects.all()
        print (product_list[0].imgURL)
    except (DataError):
        product_list = []
    else:
        pass

    context = {
        'product_list': product_list
    }
    return render(request, 'Pages/products.html', context)

def aboutUs(request):
    about = get_object_or_404(Write_up, id_name="about")
    vision_mission = get_object_or_404(Write_up, id_name="vision_mission")
    promise = get_object_or_404(Write_up, id_name="promise")
    standards = get_object_or_404(Write_up, id_name="standards")
    awards = get_object_or_404(Write_up, id_name="awards")

    context = {
        'about': about,
        'vision_mission': vision_mission,
        'promise': promise,
        'standards': standards,
        'awards': awards
    }
    return render(request, 'Pages/about.html', context)

def businessWithUs(request):
    business = get_object_or_404(Write_up, id_name="business")
    vision_mission = get_object_or_404(Write_up, id_name="vision_mission")
    expertise = get_object_or_404(Write_up, id_name="expertise")
    howLong = get_object_or_404(Write_up, id_name="how long")
    context = {
        'business': business,
        'vision_mission': vision_mission,
        'expertise': expertise,
        'howLong': howLong
    }
    return render(request, 'Pages/business.html', context)

def contact(request):
    return render(request, 'Pages/contact.html')
