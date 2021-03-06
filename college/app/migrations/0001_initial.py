# Generated by Django 3.0.8 on 2021-08-14 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('coll_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('d_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.College')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.College')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rolln', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('clg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.College')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Dept')),
                ('lec_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Lecturer')),
            ],
        ),
    ]
