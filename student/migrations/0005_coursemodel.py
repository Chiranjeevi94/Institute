# Generated by Django 3.0.8 on 2020-07-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200716_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contactno', models.IntegerField()),
                ('course', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
