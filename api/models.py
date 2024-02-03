from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=100)
    todo = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    


