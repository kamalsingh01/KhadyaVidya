# Generated by Django 4.1.7 on 2023-04-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chef_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='recipe')),
                ('recipe_type', models.CharField(choices=[('veg', 'Veg'), ('nonveg', 'Non-Veg')], max_length=10)),
            ],
        ),
    ]
