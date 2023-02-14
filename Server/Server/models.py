from django.db import models
from django.urls import reverse

# Create your models here.
class Userbase(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    tokens = models.IntegerField()



class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Userbase, on_delete=models.CASCADE)
    toppings = models.ArrayField(models.PositiveIntegerField(), size=5)
    baked = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    level = models.PositiveSmallIntegerField()
    saucy =  models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
class Pizza(models.Model):
    owner = models.ForeignKey(Userbase, on_delete=models.CASCADE)
    plate = models.IntegerField() # this represents the level of the pizza
    crust = models.FloatField() # This is how far the crust is baked
    sauce = models.IntegerField() # This is the type of sauce on the pizza
    saucy =  models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]) # This is the amount of sauce on the pizza


    def __str__(self):
        return f"{self.plate} {self.crust} {self.sauce} {self.Topping1} {self.Topping2} {self.Topping3} {self.Topping4} {self.Topping5}"

    def get_absolute_url(self):
        return reverse('pizza-detail', kwargs={'pk': self.pk})


class Topping(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('topping-detail', kwargs={'pk': self.pk})

class Crust(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crust-detail', kwargs={'pk': self.pk})

class Sauce(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sauce-detail', kwargs={'pk': self.pk})
    
class Saucy(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('saucy-detail', kwargs={'pk': self.pk})
    
class Plate(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plate-detail', kwargs={'pk': self.pk})



