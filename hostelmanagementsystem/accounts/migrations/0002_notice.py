# Generated by Django 2.2.5 on 2021-03-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
    ]
