# Generated by Django 4.1.4 on 2023-01-03 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/teamimages')),
            ],
        ),
    ]