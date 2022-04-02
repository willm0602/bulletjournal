from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    access_token = models.CharField(max_length=128, default='')

class Task(models.Model): # This is a subclass of the model.Model class
    # Define fields
    task_text = models.CharField(max_length = 200)
    completed = models.BooleanField()

    # Getter functions
    def __name__(self):
        return self.task_text
    def __done__(self):
        return self.completed
