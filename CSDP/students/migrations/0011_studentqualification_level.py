# Generated by Django 2.0.7 on 2019-11-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_remove_studentqualification_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentqualification',
            name='level',
            field=models.ManyToManyField(to='students.EduLevel'),
        ),
    ]