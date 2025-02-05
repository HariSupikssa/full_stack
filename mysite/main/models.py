from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name = "todolist")

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

