from django.shortcuts import render,redirect
from django.urls import reverse
from UserFront.models import user_reg_db,ReviewRating, user_feedback_db, hiring_sys_db,chatroom_db,message_db
from WorkerEnd.models import worker_db
from AdminEnd.models import request_reps_db,skill_db
from django.contrib import messages
from django.http import JsonResponse,HttpResponse
from django.db.models import Q,Avg
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, validate_slug
# Create your views here.

def uf_home2(request):
    work = worker_db.objects.all()
    return render(request,"uf_home.html",{'work':work})

def uf_reg_save(request):
    url = request.META.get('HTTP_REFERER')
    if request.method=="POST":
        fn = request.POST.get('uf_fn')
        ln = request.POST.get('uf_ln')
        un = request.POST.get('uf_user')
        ps = request.POST.get('uf_pass')
        m = request.POST.get('uf_mbl')
        e = request.POST.get('uf_em')

        try:
            # Validate email
            validate_email(e)

            # Validate username
            validate_slug(un)

            # Add more custom validations for password length, complexity, etc.
            if len(ps) < 8 or len(ps) > 16:
                raise ValidationError("Password should be between 8 and 16 characters.")

            if user_reg_db.objects.filter(username=un).exists():
                messages.error(request, "Username already exists. Please choose a different one.")
                return redirect(url)

            if user_reg_db.objects.filter(email=e).exists():
                messages.error(request, "Email address already exists. Please use a different one.")
                return redirect(url)

            obj = user_reg_db(first_name=fn,last_name=ln,username=un,password=ps,mobile=m,email=e)
            obj.save()

            if user_reg_db.objects.filter(username=un,password=ps).exists():
                user_instance = user_reg_db.objects.get(username=un, password=ps)
                request.session['uf_user_id'] = user_instance.id
                request.session['uf_username'] = un
                request.session['uf_password'] = ps
                messages.success(request,"Account created successfully!")
                return redirect(url)

        except ValidationError as e:
            messages.error(request, e.message)
            return redirect(url)

def uf_login_check(request):
    url = request.META.get('HTTP_REFERER')
    if request.method=="POST":
        un = request.POST.get('uf_user_l')
        ps = request.POST.get('uf_pass_l')

        try:
            user_instance = user_reg_db.objects.get(username=un, password=ps)
            request.session['uf_user_id'] = user_instance.id
            request.session['uf_username'] = un
            request.session['uf_password'] = ps
            messages.success(request, "You are logged in!")
            return redirect(url)
        except user_reg_db.DoesNotExist:
            messages.error(request, "Incorrect username/password")
            return redirect(url)
    return redirect(url)

def uf_logout(request):
    del request.session['uf_username']
    del request.session['uf_password']
    messages.success(request,"Logged out successfully!")
    return redirect(uf_home2)

def uf_wrk_prof_page(x,dataid):
    data = worker_db.objects.get(id=dataid)
    cmpl = hiring_sys_db.objects.filter(worker=dataid,if_reported=False,o_completion=True).count()
    reviews = ReviewRating.objects.filter(worker=dataid).count()
    average_rating = data.workers.aggregate(avg_rating=Avg('rating'))['avg_rating']
    context = {
        'pdet':data,
        'average_rating':average_rating,
        'reviews':reviews,
        'cmpl':cmpl
    }
    return render(x,"uf_wrk_prof.html",context)

def uf_review_save(request,dataid):
    url = request.META.get('HTTP_REFERER')
    if request.method=="POST":
        subject = request.POST.get('rr_subject')
        rating = request.POST.get('rr_star')
        review = request.POST.get('rr_review')
        username = request.POST.get('rr_username')

        # Check if any of the required fields is missing
        if not all([subject, rating, review, username]):
            messages.warning(request, 'Please fill all the required fields to submit the review!')
            return redirect(url)

        form_data = {
            'subject': subject,
            'rating': rating,
            'review': review,
            'username': username,
        }
        if 'uf_user_id' in request.session:
            user_id = request.session['uf_user_id']
        try:
            reviews = ReviewRating.objects.get(user__id=user_id,worker__id=dataid)
            reviews.subject = form_data['subject']
            reviews.rating = form_data['rating']
            reviews.review = form_data['review']
            reviews.username = form_data['username']
            reviews.worker_id = dataid
            reviews.user_id = user_id
            reviews.save()
            messages.success(request,'Thank you! Your review has been updated.')
            return redirect(url)


        except ReviewRating.DoesNotExist:
            new_review = ReviewRating(
                subject=form_data['subject'],
                rating=form_data['rating'],
                review=form_data['review'],
                username=form_data['username'],
                worker_id=dataid,
                user_id=user_id
            )
            new_review.save()

            messages.success(request, 'Thank you! Your review has been submitted.')
            return redirect(url)


def uf_contact_pg(x):
    return render(x,"uf_contact_pg.html")

def uf_con_save(x):
    if x.method == "POST":
        fn = x.POST.get('c_fname')
        ln = x.POST.get('c_lname')
        e = x.POST.get('c_email')
        mb = x.POST.get('c_mbl')
        s = x.POST.get('c_sub')
        m = x.POST.get('c_msg')
        obj = user_feedback_db(f_name=fn,l_name=ln,em=e,mbl=mb,sub=s,msg=m)
        messages.success(x,"Your feedback has been received!")
        obj.save()
        return redirect(uf_contact_pg)

def uf_hs_request(request,dataid):
    url = request.META.get('HTTP_REFERER')
    if request.method=="POST":
        form_data = {
            'sub':request.POST.get('hs_reqsub'),
            'det':request.POST.get('hs_reqdet'),
            'f_date':request.POST.get('hs_req_f_date'),
            'l_date':request.POST.get('hs_req_l_date'),
            'town':request.POST.get('hs_town'),
            'district':request.POST.get('hs_district'),
            'username':request.POST.get('hs_username'),
            'prof':request.POST.get('hs_profname'),
        }
        if 'uf_user_id' in request.session:
            user_id = request.session['uf_user_id']

        usr_request = hiring_sys_db(
            o_sub=form_data['sub'],
            o_desc=form_data['det'],
            o_f_date=form_data['f_date'],
            o_l_date=form_data['l_date'],
            o_town=form_data['town'],
            o_district=form_data['district'],
            user_name=form_data['username'],
            prof_name=form_data['prof'],
            worker_id=dataid,
            user_id=user_id
        )
        usr_request.save()
        messages.success(request, 'Your hire request has been sent!')
        return redirect(url)

def uf_requests_page(request):
    data = user_reg_db.objects.get(username=request.session['uf_username'])
    context = {
        'req':data,
        'today_date': timezone.now().strftime('%d-%m-%Y')
    }
    return render(request,"uf_my_req.html",context)

def uf_report_request(request,dataid):
    if request.method == "POST":
        reas = request.POST.get('rep_reason')
        msg = request.POST.get('rep_msg')
        obj = request_reps_db(rep_option=reas,rep_msg=msg,req_id=dataid)
        hiring_sys_db.objects.filter(id=dataid).update(if_reported=True)
        obj.save()
        messages.warning(request,"You have reported the request!")
        return redirect(uf_requests_page)

def uf_not_cmpl_report(x,dataid):
    obj = request_reps_db(rep_option="Did not complete",rep_msg="Did not complete the request even after 3 days of fixed date",req_id=dataid)
    hiring_sys_db.objects.filter(id=dataid).update(if_reported=True)
    obj.save()
    messages.warning(x,"You have reported the request!")
    return redirect(uf_requests_page)

def uf_cancel_req(x,reqID):
    data = hiring_sys_db.objects.filter(id=reqID)
    data.delete()
    messages.error(x,"The request has been cancelled")
    return redirect(uf_requests_page)

def uf_skillhivers_pg(request):
    data = worker_db.objects.all()
    return render(request,"uf_skillhivers.html",{'skillhivers':data})

def uf_autocomplete_skill(request):
    if 'term' in request.GET:
        term = request.GET.get('term', '')
        qs = skill_db.objects.filter(skill__istartswith=term)
        skills =set()
        skills.update([skill.skill.lower() for skill in qs])

        qs2 = worker_db.objects.filter(skill_2__icontains=term)
        for item in qs2:
            for skill in item.skill_2.split(','):
                stripped_skill = skill.strip()
                if stripped_skill.lower().startswith(term.lower()):
                    skills.add(stripped_skill)

        skills_fi = [skill.capitalize() for skill in skills]
        return JsonResponse(skills_fi,safe=False)

def uf_search_result(request):
    if request.method == "GET":
        skill_query = request.GET.get('skill_q')
        dist_query = request.GET.get('dist_q')

        if not dist_query and not skill_query:
            return redirect('uf_skillhivers_pg')  # Redirect to the page that lists all fields

        multi_skill = Q(skill_1__icontains=skill_query) | Q(skill_2__icontains=skill_query)
        district_filter = Q(district__icontains=dist_query)

        if skill_query and not dist_query:
            results = worker_db.objects.filter(multi_skill)
        elif dist_query and not skill_query:
            results = worker_db.objects.filter(district_filter)
        else:
            results = worker_db.objects.filter(multi_skill, district_filter)

        return render(request, "uf_skillhivers_filter.html", {'res': results})
    return redirect('uf_skillhivers_pg')

def uf_chat_msg_pg(request,room):
    room_det = chatroom_db.objects.get(room_name=room)
    skillhiver = worker_db.objects.get(id=room_det.sk_hv_id)
    return render(request,"uf_messages.html",{'room_det':room_det,'skillhiver':skillhiver})

def uf_check_room(request,userID,skhID):

    name_room = f"room-userID{userID}-skhID{skhID}"

    if chatroom_db.objects.filter(room_name=name_room).exists():
        return redirect(reverse('uf_chat_msg_pg', args=[name_room]))
    else:
        new_room = chatroom_db.objects.create(room_name=name_room,client_id=userID,sk_hv_id=skhID)
        new_room.save()
        return redirect(reverse('uf_chat_msg_pg', args=[name_room]))

def uf_send_msg(request):
    room_id = request.POST['room_id']
    message = request.POST['message']
    sender = request.POST['sender_user']

    new_msg = message_db.objects.create(msg_body=message,sender_user=sender,roomid=room_id)
    new_msg.save()
    return HttpResponse("Message sent successfully!")

def uf_getmessages(request,room):
    room_det = chatroom_db.objects.get(room_name=room)

    msgs = message_db.objects.filter(roomid=room_det.id)
    return JsonResponse({"msgs":list(msgs.values())})

def uf_chat_list(request):
    skillhiver = worker_db.objects.all()
    return render(request,"uf_chat_list.html",{'skillhiver':skillhiver})