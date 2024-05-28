from django.db import models

class Toy(models.Model):
    name = models.CharField(max_length=100)
    made_in = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.name
