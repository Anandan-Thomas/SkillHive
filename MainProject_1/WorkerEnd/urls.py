from django.urls import path
from WorkerEnd import views

urlpatterns = [
    path('wr_signup/',views.wr_signup,name="wr_signup"),
    path('wr_reg_save/',views.wr_signup_save,name="wr_reg_save"),
    path('wr_login/',views.wr_login,name="wr_login"),
    path('wr_logincheck/',views.wr_logincheck,name="wr_lg_check"),
    path('wr_logout/',views.wr_logout,name="wr_logout"),

    path('wr_landing/',views.wr_landing,name="wr_landing"),

    path('wr_prof_create_pg/',views.wr_prof_create_pg,name="wr_prof_create_pg"),
    path('wr_prof_save/',views.wr_prof_save,name="wr_prof_save"),
    path('wr_profile/',views.wr_prof_page,name="wr_profile"),
    path('wr_edit_prof/',views.wr_edit_profpage,name="wr_edit_prof"),
    path('wr_prof_upd/<str:dataid>',views.wr_prof_updation,name="wr_prod_upd"),

    path('wr_rev_tbl/',views.wr_review_tbl,name="wr_rev_tbl"),

    path('wr_user_req/',views.wr_user_req,name="wr_user_req"),
    path('wr_btn_acc/<int:dataid>',views.wr_req_accept,name="wr_btn_acc"),
    path('wr_btn_rej/<int:dataid>',views.wr_req_reject,name="wr_btn_rej"),

    path('wr_acc_req_pg/',views.wr_accepted_req_pg,name="wr_acc_reg_pg"),
    path('wr_cmpl/<int:dataid>',views.wr_request_completion,name="wr_cmpl"),
    path('wr_cmpl_pg/',views.wr_completed_req_pg,name="wr_cmpl_pg"),

    path('wr_req_reports_pg/',views.wr_req_reports_pg,name="wr_req_reports_pg"),
    path('wr_req_rep_reas_sub/<int:dataid>',views.wr_req_rep_reas_submit,name="wr_req_rep_reas_sub"),

    path('wr_chat_list/',views.wr_chat_list,name="wr_chat_list"),
    path('wr_checkroom/<int:userID>/<int:skhID>',views.wr_checkroom,name="wr_checkroom"),
    path('wr_message_pg/<str:room>',views.wr_message_pg,name="wr_message_pg"),
]