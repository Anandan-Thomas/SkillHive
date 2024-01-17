from django.shortcuts import render, redirect
from django.urls import reverse
from WorkerEnd.models import worker_login_db, worker_db
from UserFront.models import ReviewRating, hiring_sys_db, rej_rs, user_reg_db, chatroom_db, message_db
from AdminEnd.models import skill_db, request_reps_db
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, validate_slug


# Create your views here.
def wr_signup(x):
    return render(x, "wr_signup.html")


def wr_signup_save(request):
    if request.method == "POST":
        un = request.POST.get('wr_uname')
        em = request.POST.get('wr_em')
        mbl = request.POST.get('wr_mbl')
        p = request.POST.get('wr_pass')

        try:
            # Validate email
            validate_email(em)

            # Validate username
            validate_slug(un)

            # Add more custom validations for password length, complexity, etc.
            if len(p) < 8 or len(p) > 16:
                raise ValidationError("Password should be between 8 and 16 characters.")


            if worker_login_db.objects.filter(work_username=un).exists():
                messages.error(request, "Username already exists. Please choose a different one.")
                return redirect(wr_signup)

            if worker_login_db.objects.filter(email=em).exists():
                messages.error(request, "Email address already exists. Please use a different one.")
                return redirect(wr_signup)

            obj = worker_login_db(work_username=un, work_pass=p, email=em, mobile=mbl)
            obj.save()
            messages.success(request, "You have signed up successfully!")
            if worker_login_db.objects.filter(work_username=un, work_pass=p).exists():
                request.session['wr_username'] = un
                request.session['wr_password'] = p

                return redirect(wr_landing)

        except ValidationError as e:
            messages.error(request, e.message)
            return redirect('wr_signup')

        return redirect(wr_signup)


def wr_login(x):
    return render(x, "wr_signin.html")


def wr_logincheck(request):
    if request.method == "POST":
        un = request.POST.get('wr_user')
        pwd = request.POST.get('wr_pass')

        if worker_login_db.objects.filter(work_username=un, work_pass=pwd).exists():
            request.session['wr_username'] = un
            request.session['wr_password'] = pwd
            messages.success(request, "Login Successful!")
            return redirect(wr_landing)
        else:
            messages.error(request, "Username/Password not entered correctly!")
            return redirect(wr_login)
    else:
        return redirect(wr_login)


def wr_landing(request):
    data = None
    check = False
    try:
        data = worker_db.objects.get(username=request.session['wr_username'])
        check = True
    except worker_db.DoesNotExist:
        pass

    if data is not None:
        pending = hiring_sys_db.objects.filter(worker=data.id, o_status='Pending').count()
        accepted = hiring_sys_db.objects.filter(worker=data.id, o_status='Accepted', o_completion=False,
                                            if_reported=False).count()
        completed = hiring_sys_db.objects.filter(worker=data.id, o_completion=True, if_reported=False).count()
        reviews = ReviewRating.objects.filter(worker=data.id).count()
        chatrooms = chatroom_db.objects.filter(sk_hv=data.id).count()
        nr = hiring_sys_db.objects.filter(worker=data.id)
        reports = request_reps_db.objects.filter(req__in=nr, ping_status=True).count()
    else:
        pending = accepted = completed = reviews = chatrooms = nr = reports = 0

    context = {
        'data':data,
        'check': check,
        'pending': pending,
        'completed': completed,
        'chatrooms': chatrooms,
        'reviews': reviews,
        'reports': reports,
        'accepted': accepted,
    }
    return render(request, "wr_landing.html", context)


def wr_logout(request):
    del request.session['wr_username']
    del request.session['wr_password']
    messages.success(request, "Logged Out Successfully!")
    return redirect(wr_login)


def wr_prof_create_pg(x):
    skills = skill_db.objects.all()
    return render(x, "wr_prof_creation.html",{'skill': skills})


def wr_prof_save(request):
    if request.method == "POST":
        usr = request.POST.get('wr_user')
        fname = request.POST.get('wr_fname')
        lname = request.POST.get('wr_lname')
        disp_name = request.POST.get('wr_disp_name')
        dob = request.POST.get('wr_dob')
        dist = request.POST.get('wr_district')
        town = request.POST.get('wr_town')

        if 'wr_pfp' in request.FILES:
            pfp = request.FILES['wr_pfp']
        else:
            messages.error(request, "Please upload a picture.")
            return redirect('wr_prof_create_pg')

        desc = request.POST.get('wr_desc')
        main_sk = request.POST.get('cb_end')
        sec_sk = request.POST.get('oth_skill')
        mbl1 = request.POST.get('wr_mbl1')
        mbl2 = request.POST.get('wr_mbl2')
        em = request.POST.get('wr_email')

        if not (usr and fname and lname and dob and dist and town and pfp and desc and main_sk and sec_sk and mbl1 and mbl2 and em):
            messages.error(request, "Please fill in all required fields.")
            return redirect('wr_prof_create_pg')

        obj = worker_db(
            username=usr, first_name=fname, last_name=lname, disp_name=disp_name, dob=dob, district=dist,
            town=town, img=pfp, desc=desc, skill_1=main_sk, skill_2=sec_sk, mob_1=mbl1, mob_2=mbl2,
            email=em
        )
        obj.save()
        messages.success(request, "Profile Creation Successful!")
        return redirect('wr_landing')

    return redirect('wr_prof_create_pg')


def wr_prof_page(request):
    det = worker_db.objects.get(username=request.session['wr_username'])
    return render(request, "wr_profile.html", {'data': det})


def wr_edit_profpage(request):
    skills = skill_db.objects.all()
    flag = worker_db.objects.get(username=request.session['wr_username'])
    i = worker_login_db.objects.get(work_username=request.session['wr_username'])
    return render(request, "wr_edit_form.html", {'flag': flag, 'skill': skills, 'id': i})


def wr_prof_updation(request, dataid):
    if request.method == "POST":
        fname = request.POST.get('wr_fname')
        lname = request.POST.get('wr_lname')
        disp_name = request.POST.get('wr_disp_name')
        dist = request.POST.get('wr_district')
        town = request.POST.get('wr_town')
        desc = request.POST.get('wr_desc')
        main_sk = request.POST.get('cb_end')
        sec_sk = request.POST.get('oth_skill')
        mbl1 = request.POST.get('wr_mbl1')
        mbl2 = request.POST.get('wr_mbl2')
        em = request.POST.get('wr_email')
        try:
            pfp = request.FILES['wr_pfp']
            fs = FileSystemStorage()
            pic = fs.save(pfp.name, pfp)
        except MultiValueDictKeyError:
            pic = worker_db.objects.get(username=dataid).img

        worker_db.objects.filter(username=dataid).update(img=pic, first_name=fname, last_name=lname,
                                                         disp_name=disp_name, district=dist, town=town, desc=desc,
                                                         skill_1=main_sk, skill_2=sec_sk, mob_1=mbl1, mob_2=mbl2,
                                                         email=em)
        messages.success(request, "Updated successfully!")
        return redirect(wr_prof_page)


def wr_review_tbl(request):
    data = worker_db.objects.filter(username=request.session['wr_username'])
    return render(request, "wr_reviews_table.html", {'data': data})


def wr_user_req(request):
    data = worker_db.objects.get(username=request.session['wr_username'])
    return render(request, "wr_user_req.html", {'wrk': data})


def wr_req_accept(request, dataid):
    if request.method == "POST":
        fix_date = request.POST.get('hs_o_fix_date')
        hiring_sys_db.objects.filter(id=dataid).update(o_fixed_date=fix_date, o_status="Accepted")
        messages.success(request, "Request Accepted!")
        return redirect(wr_user_req)


def wr_req_reject(request, dataid):
    if request.method == "POST":
        rej_msg = request.POST.get('rej_msg')
        rej_rad = request.POST.get('rej_radio_reason')
        hiring_sys_db.objects.filter(id=dataid).update(o_status="Rejected")
        obj = rej_rs(order_id=dataid, msg=rej_msg, rad_reason=rej_rad)
        obj.save()
        messages.error(request, "Request Rejected!")
        return redirect(wr_user_req)


def wr_accepted_req_pg(request):
    data = worker_db.objects.get(username=request.session['wr_username'])
    return render(request, "wr_accepted_req.html", {'acc': data})


def wr_request_completion(request, dataid):
    hiring_sys_db.objects.filter(id=dataid).update(o_completion=True, completed_on=datetime.datetime.now())
    messages.success(request, "Request Completed!")
    return redirect(wr_accepted_req_pg)


def wr_completed_req_pg(request):
    data = worker_db.objects.get(username=request.session['wr_username'])
    return render(request, "wr_completed_req.html", {'acc': data})


def wr_req_reports_pg(request):
    data = worker_db.objects.get(username=request.session['wr_username'])
    return render(request, "wr_req_reports.html", {'det': data})


def wr_req_rep_reas_submit(x, dataid):
    if x.method == "POST":
        reason = x.POST.get('wr_report_reas')
        request_reps_db.objects.filter(id=dataid).update(prof_response=reason, prof_resp_status=True)
        messages.info(x, "Your response has been submitted!")
        return redirect(wr_req_reports_pg)


def wr_chat_list(request):
    client = user_reg_db.objects.all()
    worker = worker_db.objects.get(username=request.session['wr_username'])
    return render(request, "wr_chat_list.html", {'client': client, 'worker': worker})


def wr_message_pg(request, room):
    room_det = chatroom_db.objects.get(room_name=room)
    client = user_reg_db.objects.get(id=room_det.client_id)
    worker = worker_db.objects.get(username=request.session['wr_username'])
    return render(request, "wr_message.html", {'room_det': room_det, 'client': client, 'worker': worker})


def wr_checkroom(request, userID, skhID):
    name_room = f"room-userID{userID}-skhID{skhID}"

    if chatroom_db.objects.filter(room_name=name_room).exists():
        return redirect(reverse('wr_message_pg', args=[name_room]))
    else:
        return redirect(wr_chat_list)

# def wr_sendmsg(request):
#     room_id = request.POST['room_id']
#     message = request.POST['message']
#     sender = request.POST['sender_user']
#
#     new_msg = message_db.objects.create(msg_body=message, sender_user=sender, roomid=room_id)
#     new_msg.save()
#     return HttpResponse("Message sent successfully!")

# Using the uf views itself for sending and getting messages

# def wr_getmsgs(request,room):
#     room_det = chatroom_db.objects.get(room_name=room)
#
#     msgs_sk = message_db.objects.filter(roomid=room_det.id)
#     return JsonResponse({"msgs_sk": list(msgs_sk.values())})
