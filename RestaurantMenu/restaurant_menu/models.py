from django.db import models
from django.contrib.auth.models import User
# Create your models here.
MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts'),
)
STATUS = (
    (1, 'Available'),
    (2, 'Not Available'),
)


class MenuItem(models.Model):
    meal = models.CharField(max_length=1000)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    status = models.IntegerField(choices=STATUS, default=1)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
