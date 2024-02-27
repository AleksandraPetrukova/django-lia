from django.shortcuts import render, redirect
from cats.models import Breed, Cat
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    cats = Cat.objects.all()
    breeds = Breed.objects.all()
    context = {
        "cats": cats,
        "breeds": breeds
    }
    return render(request, "cats/index.html", context)

def cat_details(request, cat_id):
    try:
        cat = Cat.objects.get(id=cat_id)
    except Cat.DoesNotExist:
        raise Http404("Cat does not exist")
    context = {
        "cat": cat
    }
    return render(request, "cats/cat.html", context)

def add_cat (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        description = request.POST.get('description')
        breed_id = request.POST.get('breed')
        breed = Breed.objects.get(id=breed_id)
        new_cat = Cat(name=name, age=age, weight=weight, description=description, breed=breed)
        new_cat.save()
    return redirect('cats')