from django.db import models
from django.urls import reverse

# Create your models here.
class Pizza(models.Model):
    plate = models.IntegerField()
    crust = models.FloatField()
    sauce = models.IntegerField()
    cheese = models.IntegerField()
    Topping1 = models.IntegerField()
    Topping2 = models.IntegerField()
    Topping3 = models.IntegerField()
    Topping4 = models.IntegerField()
    Topping5 = models.IntegerField()

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



