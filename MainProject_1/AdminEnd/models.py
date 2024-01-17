from django.db import models
from UserFront.models import hiring_sys_db
# Create your models here.
class skill_db(models.Model):
    skill = models.CharField(max_length=150,null=True,blank=True)

class request_reps_db(models.Model):
    req = models.ForeignKey(hiring_sys_db,on_delete=models.CASCADE,related_name="user_req")
    rep_msg = models.TextField(max_length=300,null=True,blank=True)
    rep_option = models.CharField(max_length=200,null=True,blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True)
    ping_status = models.BooleanField(default=False)
    report_update = models.DateField(null=True,blank=True)
    prof_response = models.TextField(max_length=300,null=True,blank=True)
    prof_resp_status = models.BooleanField(default=False)
    waiver_black = models.CharField(default=None,null=True,blank=True,max_length=20)
