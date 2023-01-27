#Function that generates a random pizza

def random_pizza():
    pizza = Pizza()
    pizza.plate = random.randint(1, 2)
    pizza.crust = random.randint(1, 100)
    pizza.sauce = random.randint(1, 100)
    pizza.cheese = random.randint(1, 100)
    pizza.Topping1 = random.randint(1, 100)
    pizza.Topping2 = random.randint(1, 100)
    pizza.Topping3 = random.randint(1, 100)
    pizza.Topping4 = random.randint(1, 100)
    pizza.Topping5 = random.randint(1, 100)
    pizza.save()
    return pizza

