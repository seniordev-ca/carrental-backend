# Generated by Django 3.0.1 on 2019-12-31 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentalApp', '0016_auto_20191231_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='date_time_happened',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]