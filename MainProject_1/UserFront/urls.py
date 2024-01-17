from django.urls import path
from UserFront import views

urlpatterns = [
    path('',views.uf_home2,name="uf_home2"),

    path('uf_reg_save/',views.uf_reg_save,name="uf_reg_save"),
    path('uf_log_check/',views.uf_login_check,name="uf_login_check"),
    path('uf_logout/',views.uf_logout,name="uf_logout"),

    path('uf_wrk_pro/<str:dataid>',views.uf_wrk_prof_page,name="uf_wrk_pro"),
    path('uf_review_save/<int:dataid>',views.uf_review_save,name="uf_review_save"),
    path('uf_hs_req/<int:dataid>',views.uf_hs_request,name="uf_hs_req"),

    path('uf_contact_pg/',views.uf_contact_pg,name="uf_contact_pg"),
    path('uf_con_save/',views.uf_con_save,name="uf_con_save"),

    path('uf_req_pg/',views.uf_requests_page,name="uf_req_pg"),
    path('uf_report_req/<int:dataid>',views.uf_report_request,name="uf_report_req"),
    path('uf_not_cmpl_report/<int:dataid>',views.uf_not_cmpl_report,name="uf_n_cmpl_rep_req"),
    path('uf_cancel_req/<int:reqID>',views.uf_cancel_req,name="uf_cancel_req"),

    path('uf_skillhivers_pg/',views.uf_skillhivers_pg,name="uf_skillhivers_pg"),
    path('uf_search_result/',views.uf_search_result,name="uf_search_result"),

    path('uf_autocomplete_skill/',views.uf_autocomplete_skill,name="uf_autocomplete_skill"),

    path('uf_chat_msg_pg/<str:room>',views.uf_chat_msg_pg,name="uf_chat_msg_pg"),
    path('uf_check_room/<int:userID>/<int:skhID>',views.uf_check_room,name="uf_check_room"),
    path('uf_send_msg',views.uf_send_msg,name="uf_send_msg"),
    path('uf_getmessages/<str:room>',views.uf_getmessages,name="uf_getmessages"),
    path('uf_chat_list/',views.uf_chat_list,name="uf_chat_list"),

]