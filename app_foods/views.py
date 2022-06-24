from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Food


# Create your views here.
def foods(request):
    all_foods = Food.objects.order_by('-is_premium')
    context = {'foods' : all_foods}
    return render(request,'app_foods/foods.html',context)

def food(request,food_id):
    one_food = None
    try:
        one_food = Food.objects.get(id=food_id)
    except:
        print('ไม่พบข้อมูล')
    context= { 'food' : one_food}
    return render(request, 'app_foods/food.html', context)