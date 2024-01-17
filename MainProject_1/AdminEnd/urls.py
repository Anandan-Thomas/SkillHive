from django.urls import path
from AdminEnd import views

urlpatterns =[
    path('adm_signin/',views.admin_signin,name="adm_signin"),
    path('adm_landing/',views.admin_landing,name="adm_landing"),
    path('adm_signin_check/',views.adm_login_check,name="adm_lgn_check"),
    path('adm_logout/',views.adm_logout,name="adm_logout"),

    path('adm_wrk_table/',views.adm_wrk_table,name="adm_wrk_table"),
    path('adm_wrk_prof/<str:dataid>',views.adm_wrk_profile,name="adm_wrk_prof"),
    path('adm_disable/<str:sk_user>',views.adm_disbale_acc,name="adm_disable"),
    path('adm_enable/<str:sk_user>',views.adm_enable_acc,name="adm_enable"),
    path('adm_delete_worker/<int:wID>',views.adm_delete_worker,name="adm_delete_worker"),

    path('adm_skill_table/',views.adm_skill_table,name="adm_skill_table"),
    path('adm_add_skill/',views.adm_add_skill,name="adm_add_skill"),
    path('adm_upd_skill/<int:skillID>',views.adm_upd_skill,name="adm_upd_skill"),
    path('adm_del_skill/<int:skillID>',views.adm_del_skill,name="adm_del_skill"),

    path('adm_user_table/',views.adm_user_table,name="adm_user_table"),
    path('adm_delete_user/<int:userID>',views.adm_delete_user,name="adm_delete_user"),


    path('adm_request_rep_pg/',views.adm_report_req_page,name="adm_report_req_pg"),
    path('adm_req_ping_prof/<int:dataid>',views.adm_req_ping_prof,name="adm_rq_ping"),
    path('adm_req_black_point/<int:profID>/<int:repID>',views.adm_req_black_point,name="adm_req_black_point"),
    path('adm_req_waiver/<int:repID>/<int:reqID>',views.adm_req_waiver,name="adm_req_waiver"),

    path('adm_fb/',views.adm_fb_pg,name="adm_fb"),

]