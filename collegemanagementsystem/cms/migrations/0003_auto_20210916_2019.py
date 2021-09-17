# Generated by Django 3.0.8 on 2021-09-16 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20210916_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='bran_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Branch'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='clg_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.College'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='dep_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Depart'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='lect_sal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Salary'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Subject'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='time_table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.TimeTable'),
        ),
    ]
