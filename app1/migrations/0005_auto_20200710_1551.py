# Generated by Django 3.0.8 on 2020-07-10 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200710_0856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classmodel',
            old_name='name',
            new_name='course',
        ),
    ]
