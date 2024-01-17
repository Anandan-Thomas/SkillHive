import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.db.models import F
from WorkerEnd.models import worker_login_db,worker_db
from AdminEnd.models import skill_db,request_reps_db
from UserFront.models import user_reg_db,user_feedback_db,hiring_sys_db
from django.contrib import messages
# Create your views here.
def admin_landing(x):
    users = user_reg_db.objects.all().count()
    feedback = user_feedback_db.objects.all().count()
    pending = request_reps_db.objects.filter(waiver_black=None).count()
    skills = skill_db.objects.all().count()
    act_sk = worker_db.objects.filter(is_disabled=False).count()
    dis_sk = worker_db.objects.filter(is_disabled=True).count()

    context = {
        'users':users,
        'feedback':feedback,
        'pending':pending,
        'skills':skills,
        'act_sk':act_sk,
        'dis_sk':dis_sk
    }
    return render(x,"landing.html",context)

def admin_signin(x):
    return render(x,"adm_signin.html")

def adm_login_check(request):
    if request.method=="POST":
        un=request.POST.get('ad_user')
        pwd=request.POST.get('ad_pass')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pwd)
            if user is not None:
                request.session['adm_username'] = un
                request.session['adm_password'] = pwd
                messages.success(request,"Logged in successfully!")
                return redirect(admin_landing)
            else:
                messages.error(request,"Incorrect Username/Password!")
                return redirect(admin_signin)
    messages.error(request,"Incorrect Username/Password!")
    return redirect(admin_signin)

def adm_logout(request):
    del request.session['adm_username']
    del request.session['adm_password']
    messages.success(request,"Logged out successfully!")
    return redirect(admin_signin)

def adm_wrk_table(x):
    data = worker_login_db.objects.all()
    return render(x,"adm_worker_table.html",{'work':data})

def adm_wrk_profile(x,dataid):
    prof = worker_db.objects.get(username=dataid)
    return render(x,"adm_worker_profile.html",{'prof':prof})

def adm_skill_table(x):
    data = skill_db.objects.all()
    return render(x,"adm_prof_skill_table.html",{'skill':data})

def adm_add_skill(x):
    if x.method=="POST":
        n = x.POST.get('sk_nm')
        obj = skill_db(skill=n)
        obj.save()
        messages.success(x,"Added new skill!")
        return redirect(adm_skill_table)

def adm_del_skill(x,skillID):
    data = skill_db.objects.filter(id=skillID)
    data.delete()
    messages.warning(x,"Skill Deleted!")
    return redirect(adm_skill_table)

def adm_upd_skill(x,skillID):
    if x.method == "POST":
        skill_name = x.POST.get('skill_name')
        skill_db.objects.filter(id=skillID).update(skill=skill_name)
        messages.success(x,"Skill name updated!")
        return redirect(adm_skill_table)

def adm_user_table(x):
    users = user_reg_db.objects.all()
    return render(x,"adm_user_table.html",{'users':users})

def adm_fb_pg(x):
    data = user_feedback_db.objects.all()
    return render(x,"adm_fb_table.html",{'data':data})

def adm_report_req_page(x):
    data = hiring_sys_db.objects.all()
    return render(x,"adm_requests_report.html",{'data':data})

def adm_req_ping_prof(x,dataid):
    request_reps_db.objects.filter(id=dataid).update(ping_status=True,report_update=datetime.datetime.now())
    messages.warning(x,"Pinged!")
    return redirect(adm_report_req_page)

def adm_req_black_point(request,profID,repID):
    url = request.META.get('HTTP_REFERER')
    data = worker_db.objects.get(id=profID)
    data.black_points = F('black_points') + 1
    data.save()
    request_reps_db.objects.filter(id=repID).update(waiver_black="black",report_update=datetime.datetime.now())
    messages.warning(request, "Black Point marked!")
    return redirect(url)

def adm_req_waiver(request,repID,reqID):
    url = request.META.get('HTTP_REFERER')
    request_reps_db.objects.filter(id=repID).update(waiver_black="waiver",report_update=datetime.datetime.now())
    hiring_sys_db.objects.filter(id=reqID).update(if_reported=False)
    messages.warning(request, "Report waived off!")
    return redirect(url)

def adm_disbale_acc(request,sk_user):
    worker_login_db.objects.filter(work_username=sk_user).update(is_disabled=True)
    worker_db.objects.filter(username=sk_user).update(is_disabled=True)
    return redirect(adm_wrk_table)

def adm_enable_acc(request,sk_user):
    worker_login_db.objects.filter(work_username=sk_user).update(is_disabled=False)
    worker_db.objects.filter(username=sk_user).update(is_disabled=False,black_points=0)
    return redirect(adm_wrk_table)

def adm_delete_user(request,userID):
    data = user_reg_db.objects.get(id=userID)
    data.delete()
    messages.warning(request,"You have deleted the user!")
    return redirect(adm_user_table)

def adm_delete_worker(request, wID):
    data = worker_login_db.objects.get(id=wID)
    data2 = worker_db.objects.get(username=data.work_username)
    data2.delete()
    data.delete()

    messages.warning(request,"You have deleted the skillhiver!")
    return redirect(adm_wrk_table)