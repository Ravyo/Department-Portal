# Generated by Django 2.0.7 on 2019-11-01 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_remove_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentqualification',
            name='level',
        ),
        migrations.AddField(
            model_name='studentqualification',
            name='level',
            field=models.OneToOneField(default=10, on_delete=django.db.models.deletion.CASCADE, to='students.EduLevel'),
            preserve_default=False,
        ),
    ]
