# Generated by Django 3.0.8 on 2020-07-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmodel',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
