from django.db import models

# Create your models here.


class ToDo(models.Model):
    text = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
          return self.text


 