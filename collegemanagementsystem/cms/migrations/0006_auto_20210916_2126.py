# Generated by Django 3.0.8 on 2021-09-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20210916_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='coll_fee',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='exam_fee',
            field=models.IntegerField(null=True),
        ),
    ]