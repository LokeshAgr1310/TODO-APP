from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.title
