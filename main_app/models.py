from django.db import models

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Make: " + self.name

    class Meta:
        ordering = ['name']

# below Artist Model

class CarModel(models.Model):

    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="carmodels")
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    def formatted_price(self):
        return f"${self.price:,}"

class Collection(models.Model):
    title = models.CharField(max_length=150)
    carmodels = models.ManyToManyField(CarModel)

    def __str__(self):
        return self.title
