from django.db import models

class FoodType(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Food(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    idtype = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name
