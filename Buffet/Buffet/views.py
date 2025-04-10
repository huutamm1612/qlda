from django.shortcuts import render
from foodadd.models import Food, FoodType

def home(request):
    foodtypes = FoodType.objects.all()
    foods_by_category = {
        foodtype.name: list(Food.objects.filter(idtype=foodtype).values('name', 'price'))
        for foodtype in foodtypes
    }
    return render(request, 'Buffet/home.html', {'foods_by_category': foods_by_category})
