# Generated by Django 4.0.3 on 2022-04-02 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_habit_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='dates',
            field=models.JSONField(default={}),
        ),
    ]