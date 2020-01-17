from django.db import models

# Create your models here.
# Create your models here.
# Create your models here.
from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)
    student_id = models.CharField(primary_key=True, max_length=6, null=False)
    roll = models.CharField(null=False,max_length=10)
    semester=models.CharField(null=False,max_length=10)
    section=models.CharField(null=False,max_length=10)
    registration = models.IntegerField(null=False)
    phone = models.CharField(null=True, max_length=11)
    session_start = models.DateField(verbose_name=u"Session start")
    session_end = models.DateField(verbose_name=u"Session end")



    def session(self, start, end):
        self.start = session_start
        self.end = session_end
        return f"{self.start} to {self.end}"

    def __str__(self):
        return f"{self.name} "

class StudentInfo(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    gender = models.CharField(max_length=7)
    dateOfBirth = models.DateField()
    email = models.EmailField(max_length=30)
    courses=models.TextField(max_length=400)
    Address = models.CharField(max_length=80)
    description = models.TextField(max_length=400)


    def __str__(self):
        return str(self.name)

class EduLevel(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    Qualification=models.CharField(max_length=10)
    Percentage=models.IntegerField()
    yearCompleted = models.DateField()
    instituteName = models.CharField(max_length=100)

class StudentQualification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    level = models.ManyToManyField(EduLevel)

    def __str__(self):
        return str(self.student)

