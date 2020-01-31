# Generated by Django 3.0.1 on 2020-01-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentalApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartype',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='cartype',
            name='price_per_year',
        ),
        migrations.AddField(
            model_name='cartype',
            name='price_per_year_eur',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cartype',
            name='price_per_year_usd',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='user_app_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='damaged_part',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='car_type_id',
            field=models.IntegerField(null=True),
        ),
    ]