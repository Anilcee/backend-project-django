# Generated by Django 4.1.2 on 2022-11-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_ourservices_servicedesc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='clientComment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
