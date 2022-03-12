# Generated by Django 2.2.5 on 2021-03-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210308_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_dob',
        ),
        migrations.RemoveField(
            model_name='student',
            name='u_name',
        ),
        migrations.AddField(
            model_name='student',
            name='add_area',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='add_city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='add_state',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='b_date',
            field=models.DateField(null='true'),
            preserve_default='true',
        ),
        migrations.AddField(
            model_name='student',
            name='mobile_no',
            field=models.CharField(max_length=10, null='true'),
            preserve_default='true',
        ),
        migrations.AddField(
            model_name='student',
            name='s_age',
            field=models.IntegerField(null='true'),
            preserve_default='true',
        ),
        migrations.AddField(
            model_name='student',
            name='s_email',
            field=models.EmailField(max_length=100, null='true'),
            preserve_default='true',
        ),
        migrations.AddField(
            model_name='student',
            name='s_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null='true'),
            preserve_default='true',
        ),
        migrations.AddField(
            model_name='student',
            name='s_sem',
            field=models.IntegerField(null='true'),
            preserve_default='true',
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=100),
        ),
    ]
