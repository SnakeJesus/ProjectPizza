from django.shortcuts import render
import random
from django.http import JsonResponse
from .models import Userbase, Pizza, Topping

def get_user_data(request):
    username = request.GET.get('username')
    try:
        user = Userbase.objects.get(name=username)
        pizzas = Pizza.objects.filter(owner=user)
        data = {
            'tokens': user.tokens,
            'pizzas': [{
                'toppings': [topping.pk for topping in pizza.toppings.all()],
                'baked': pizza.baked,
                'level': pizza.level
            } for pizza in pizzas]
        }
        return JsonResponse(data)
    except Userbase.DoesNotExist:
        return JsonResponse({'error': 'User not found'})
    
User = get_user_model()

def generate_pizza(request, username):
    user = User.objects.get(name=username)
    if user.tokens < 1:
        return JsonResponse({'error': 'Not enough tokens'})
    
    toppings = Topping.objects.all()
    random_toppings = random.sample(list(toppings), 5)
    new_pizza = Pizza.objects.create(owner=user, baked=random.uniform(0, 1), level=random.randint(0, 10))
    new_pizza.toppings.set(random_toppings)
    user.tokens -= 1
    user.save()

    user_data = {
        'name': user.name,
        'tokens': user.tokens,
        'pizzas': list(user.pizza_set.values())
    }

    return JsonResponse(user_data)