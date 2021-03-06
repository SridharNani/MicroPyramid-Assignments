# Generated by Django 3.0.8 on 2021-09-16 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20210916_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='clg_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.College'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_role',
            field=models.CharField(blank=True, choices=[('Puene', 'Puene'), ('Attender', 'Attender'), ('Swepaer', 'Sweaper'), ('Watchman', 'Watchman')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_salary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Salary'),
        ),
    ]
