# Generated by Django 2.0.7 on 2019-11-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20191101_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentqualification',
            name='level',
        ),
        migrations.AddField(
            model_name='studentqualification',
            name='level',
            field=models.ManyToManyField(to='students.EduLevel'),
        ),
    ]
