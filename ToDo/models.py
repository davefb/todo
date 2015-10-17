from django.db import models


class ToDo(models.Model):
    pass

class ToDoItem(models.Model):
    parent = models.ForeignKey(ToDo,related_name="items")
    item_text = models.CharField(max_length=1000)


