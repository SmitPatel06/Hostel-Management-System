# Generated by Django 2.2.5 on 2021-03-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210310_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='created_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]