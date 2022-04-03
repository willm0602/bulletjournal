from datetime import datetime

from django.db import models

from frontend.utils import date_format_to_string, string_to_date_format


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    access_token = models.CharField(max_length=128, default="")


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dates = models.JSONField(default={})

    def add_date(self, date=datetime.today):
        date = date_format_to_string(date)
        self.dates[date] = True

    def remove_date(self, date=datetime.today):
        date = date_format_to_string(date)
        self.dates[date] = False

    def contains_date(self, target_date: datetime):
        target_date = date_format_to_string(target_date)
        dates: models.JSONField = self.dates
        for date, valid in dates.items():
            if valid and date == target_date:
                return True
        return False


class Task(models.Model):  # This is a subclass of the model.Model class
    # Define fields
    task_text = models.CharField(max_length=200)
    completed = models.BooleanField()
    
    # Getter functions
    def __name__(self):
        return self.task_text

    def __done__(self):
        return self.completed


class Calendar_Task(models.Model):
    task_text = models.CharField(max_length=200)
    completed = models.BooleanField()

    @property
    def __name__(self):
        return self.task_text

    @property
    def __completed__(self):
        return self.completed
