# Generated by Django 2.0.7 on 2019-11-01 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20191101_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentqualification',
            name='level',
            field=models.ManyToManyField(to='students.EduLevel'),
        ),
        migrations.AlterField(
            model_name='studentqualification',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
    ]