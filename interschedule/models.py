from django.db import models

# Create your models here.
class interviewee(models.Model):
  interviewee_id=models.IntegerField(primary_key=True)
  f_name=models.CharField(max_length=30,verbose_name="FirstName")
  l_name=models.CharField(max_length=30,verbose_name="LastName",null=True,blank=True)
  email=models.CharField(max_length=40)
  resume=models.URLField(max_length=200,null=True,blank=True)

  def __str__(self):
    return self.f_name+" "+self.l_name

class interview(models.Model):
  st_time=models.DateTimeField()
  end_time=models.DateTimeField()
  interviewees=models.ManyToManyField(interviewee)

  class Meta:
        ordering = ('st_time',)

  def __str__(self):
    return str(self.st_time)+" "+str(self.end_time)