
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.CharField(max_length=9,unique=True,primary_key=True)
    department=models.CharField(max_length=50, blank=True,null=True)
    user_photo=models.CharField(max_length=50, blank=True,null=True)
    user_rating=models.IntegerField(default=0)
    is_blocked=models.BooleanField(default=False)
    block_date=models.DateTimeField(blank=True,null=True)


class Courses(models.Model):
    course_id=models.CharField(max_length=6)
    course_description=models.CharField(max_length=200)
    course_department=models.CharField(max_length=50)
    course_difficulty=models.IntegerField()
    course_workload=models.IntegerField()
    course_content_rating=models.IntegerField()
    course_review=models.CharField(max_length=200)

    def __str__(self):
        return(self.course_id)

class Professors(models.Model):
    prof_name=models.CharField(max_length=50)
    prof_deparment=models.CharField(max_length=50)
    prof_research_interest=models.CharField(max_length=50,blank=True)
    img_src=models.CharField(max_length=100,blank=True,default='')
    website=models.CharField(max_length=100,blank=True,default="")

    def __str__(self):
        return(self.prof_name)

class ProfRating(models.Model):
    prof_name=models.ForeignKey(Professors, on_delete=models.CASCADE)
    punctuality=models.IntegerField()
    grading=models.IntegerField()
    strictness=models.IntegerField()
    teaching_skill=models.IntegerField()
    enthusiasmInTeaching=models.IntegerField()
    overall=models.IntegerField()
    review=models.CharField(max_length=200,blank=True,default="")

    def __str__(self):
        return self.overall


class TaughtBy(models.Model):
    prof_name=models.ForeignKey(Professors, on_delete=models.CASCADE,related_name="prof")
    course_id=models.ForeignKey(Courses, on_delete=models.CASCADE,related_name="course")
    rating=models.IntegerField()
    review=models.CharField(max_length=200,blank=True,default="")
    def __str__(self):
        return (self.prof_name.prof_name+" teaches " +  self.course_id.course_id)





    