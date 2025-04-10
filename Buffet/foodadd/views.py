from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, FoodType
from django.http import HttpResponse

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'foodadd/food_list.html', {'foods': foods})

def add_food(request):
    if request.method == 'POST':
        id = request.POST['id']
        idtype = request.POST['idtype']
        name = request.POST['name']
        price = request.POST['price']
        Food.objects.create(id=id, idtype_id=idtype, name=name, price=price)
        return redirect('food_list')
    foodtypes = FoodType.objects.all()
    return render(request, 'foodadd/add_food.html', {'foodtypes': foodtypes})

def add_food_type(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        FoodType.objects.create(id=id, name=name)
        return redirect('food_list')
    return render(request, 'foodadd/add_food_type.html')

def edit_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        food.name = request.POST['name']
        food.price = request.POST['price']
        food.idtype_id = request.POST['idtype']
        food.save()
        return redirect('food_list')
    foodtypes = FoodType.objects.all()
    return render(request, 'foodadd/edit_food.html', {'food': food, 'foodtypes': foodtypes})

def delete_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    food.delete()
    return redirect('food_list')

def home(request):
    foodtypes = FoodType.objects.all()
    foods_by_category = {foodtype.name: Food.objects.filter(idtype=foodtype) for foodtype in foodtypes}
    return render(request, 'foodadd/home.html', {'foods_by_category': foods_by_category})
