from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Dish, Reservation, Review, Category
# Create your views here.
def hello(request):
    return HttpResponse("hello World")

def mainpage(request):
    return render(request,"main2.html")

def dishlist(request):
    dishes = Dish.objects.all()
    return render(request,"dishes.html",{"dishes":dishes})

def dishdetail(request, slug):
    dish = get_object_or_404(Dish,slug=slug)
    return render(request,"dishdetail.html",{"dish":dish})

def reviewlist(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html",{"reviews":reviews})

