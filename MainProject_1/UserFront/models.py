from django.db import models
from WorkerEnd.models import worker_db
import datetime
# Create your models here.

class user_reg_db(models.Model):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)


class ReviewRating(models.Model):
    worker= models.ForeignKey(worker_db, on_delete=models.CASCADE, related_name="workers")
    user= models.ForeignKey(user_reg_db, on_delete=models.CASCADE, related_name="users")
    subject = models.CharField(max_length=140, blank=True, null=True)
    review = models.TextField(max_length=500,blank=True,null=True)
    rating = models.FloatField(null=True,blank=True)
    status = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=150,blank=True,null=True)


class user_feedback_db(models.Model):
    f_name = models.CharField(max_length=100,null=True,blank=True)
    l_name = models.CharField(max_length=100,null=True,blank=True)
    em = models.CharField(max_length=100,null=True,blank=True)
    mbl = models.IntegerField(null=True,blank=True)
    sub = models.CharField(max_length=140,null=True,blank=True)
    msg = models.TextField(max_length=500,null=True,blank=True)
    fb_sent = models.DateTimeField(auto_now_add=True)

class hiring_sys_db(models.Model):
    worker = models.ForeignKey(worker_db, on_delete=models.CASCADE, related_name="ord_wrk")
    user = models.ForeignKey(user_reg_db, on_delete=models.CASCADE, related_name="ord_usr")
    o_sub = models.CharField(max_length=100,null=True,blank=True)
    o_desc = models.TextField(max_length=500,null=True,blank=True)
    o_f_date = models.DateField(null=True,blank=True)
    o_l_date = models.DateField(null=True,blank=True)
    o_fixed_date = models.DateField(null=True,blank=True)
    o_status = models.CharField(max_length=50,null=True,blank=True,default="Pending")
    o_town = models.CharField(max_length=50,null=True,blank=True)
    o_district = models.CharField(max_length=50,null=True,blank=True)
    o_completion = models.BooleanField(default=False)
    user_name = models.CharField(max_length=120,null=True,blank=True)
    prof_name = models.CharField(max_length=120,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateField(null=True,blank=True)
    if_reported = models.BooleanField(default=False)

class rej_rs(models.Model):
    order = models.ForeignKey(hiring_sys_db,on_delete=models.CASCADE,related_name="rej_order")
    msg = models.TextField(max_length=300,null=True,blank=True)
    rad_reason = models.CharField(max_length=60,null=True,blank=False)
    rej_date = models.DateTimeField(auto_now_add=True)


class chatroom_db(models.Model):
    room_name = models.CharField(max_length=200)
    client = models.ForeignKey(user_reg_db,on_delete=models.CASCADE,related_name="room_client")
    sk_hv = models.ForeignKey(worker_db,on_delete=models.CASCADE,related_name="room_skh")

class message_db(models.Model):
    msg_body = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    sender_user = models.CharField(max_length=50)
    roomid = models.IntegerField()

