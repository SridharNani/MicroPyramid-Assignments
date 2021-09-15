# Generated by Django 3.0.8 on 2021-09-14 13:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_lecturer', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('bran_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=20)),
                ('clg_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.College')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('First class', 'Grade A'), ('second class', 'Grade B2'), ('Third class', 'Grade C1'), ('fourth class', 'Grade C2'), ('Destiniction', 'Grade D1')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=20)),
                ('coll_fee', models.IntegerField()),
                ('exam_fee', models.IntegerField()),
                ('bran_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Branch')),
                ('clg_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.College')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Depart')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Results')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Subject')),
                ('time_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.TimeTable')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('staff_role', models.CharField(choices=[('Puene', 'Puene'), ('Attender', 'Attender'), ('Swepaer', 'Sweaper'), ('Watchman', 'Watchman')], max_length=20)),
                ('clg_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.College')),
                ('staff_salary', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Salary')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lect_name', models.CharField(max_length=20)),
                ('bran_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Branch')),
                ('clg_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.College')),
                ('dep_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Depart')),
                ('lect_sal', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Salary')),
                ('subject', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Subject')),
                ('time_table', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.TimeTable')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='clg_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.College'),
        ),
        migrations.AddField(
            model_name='branch',
            name='dep_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Depart'),
        ),
    ]
