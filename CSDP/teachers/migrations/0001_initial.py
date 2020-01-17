# Generated by Django 2.2.5 on 2019-09-06 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EduLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=15)),
                ('yearCompleted', models.DateField()),
                ('instituteName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('techer_id', models.CharField(max_length=6, null=True, unique=True)),
                ('designation', models.CharField(max_length=30)),
                ('joined', models.DateField(verbose_name='Year-Month')),
                ('phone', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ManyToManyField(to='teachers.EduLevel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('gender', models.CharField(max_length=7)),
                ('qualification', models.CharField(max_length=20)),
                ('dateOfBirth', models.DateField()),
                ('shortBio', models.CharField(max_length=85)),
                ('email', models.EmailField(max_length=30)),
                ('homeDistrict', models.CharField(max_length=20)),
                ('currentLocation', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=400)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='edulevel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
    ]