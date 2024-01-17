from django.db import models

# Create your models here.
class worker_db(models.Model):
    username=models.CharField(max_length=150,null=True,blank=True)
    first_name=models.CharField(max_length=150,null=True,blank=True)
    last_name=models.CharField(max_length=150,null=True,blank=True)
    disp_name=models.CharField(max_length=130,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    district=models.CharField(max_length=130,null=True,blank=True)
    town=models.CharField(max_length=130,null=True,blank=True)
    img = models.ImageField(upload_to="workers_pic", null=True, blank=True)
    desc=models.CharField(max_length=400,null=True,blank=True)
    skill_1=models.CharField(max_length=400,null=True,blank=True)
    skill_2=models.CharField(max_length=120, null=True,blank=True)
    mob_1=models.IntegerField(null=True,blank=True)
    mob_2=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=120,null=True,blank=True)
    black_points = models.IntegerField(default=0)
    is_disabled = models.BooleanField(default=False)


    def skill_1_list(self):
        return [skill.strip() for skill in self.skill_1.split(',')]

    def skill_2_list(self):
        return [skill.strip() for skill in self.skill_2.split(',')]

class worker_login_db(models.Model):
    work_username = models.CharField(max_length=150,null=True,blank=True)
    work_pass = models.CharField(max_length=150,null=True,blank=True)
    email = models.CharField(max_length=150,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    is_disabled = models.BooleanField(default=False)