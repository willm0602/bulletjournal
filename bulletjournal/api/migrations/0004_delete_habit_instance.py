# Generated by Django 4.0.3 on 2022-04-02 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_habit_habit_instance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Habit_Instance',
        ),
    ]