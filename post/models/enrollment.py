from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    student = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    name = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    final_grade = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name    

    class Meta:
        unique_together = [['course', 'student']]