# Generated by Django 4.0.5 on 2022-06-21 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0001_initial'),
        ('app_gen', '0003_alter_subscription_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='food',
        ),
        migrations.AddField(
            model_name='subscription',
            name='food_set',
            field=models.ManyToManyField(to='app_foods.food'),
        ),
    ]