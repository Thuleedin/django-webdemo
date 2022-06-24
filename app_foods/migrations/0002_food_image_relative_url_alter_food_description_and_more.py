# Generated by Django 4.0.5 on 2022-06-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image_relative_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='promotion_end_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='special_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]