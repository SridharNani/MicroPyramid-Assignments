# Generated by Django 3.0.8 on 2021-08-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30)),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
    ]