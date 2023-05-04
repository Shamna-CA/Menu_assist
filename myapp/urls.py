from django.urls import path
from myapp import views

urlpatterns = [

    path('login_fun/', views.login_fun),
    path('login_post/', views.login_fun_post),
    # path('signup/', views.signup),
    path('a_change_pswd/', views.a_change_pswd),
    path('a_change_pswd_post/', views.a_change_pswd_post),
    path('add_menu/', views.add_menu),
    path('add_menu_post/', views.add_menu_post),
    path('v_menu/', views.v_menu),
    path('v_menu_post/', views.v_menu_post),
    path('delete_menu/<mid>', views.delete_menu),
    path('edit_menu/<mid>', views.edit_menu),
    path('edit_menu_post/', views.edit_menu_post),
    path('v_feedback/', views.v_feedback),
    path('v_complaint/', views.v_complaint),
    path('send_reply/<str:mid>', views.send_reply),
    path('send_reply_post/', views.send_reply_post),
    path('v_ordr_rprt/', views.v_ordr_rprt),
    path('v_rating_food/', views.v_rating_food),
    path('v_staff/', views.v_staff),
    path('v_staff_post/', views.v_staff_post),
    path('a_staff/', views.add_staff),
    path('delete_staff/<mid>', views.delete_staff),
    path('e_staff/<mid>', views.edit_staff),
    path('edit_staff_post/', views.edit_staff_post),
    path('add_staff_post/', views.add_staff_post),
    path('add_tdys_menu/', views.add_tdys_menu),
    path('add_tdys_menu_post/', views.add_tdys_menu_post),
    path('delete_tdys_menu/<mid>', views.delete_tdys_menu),
    path('v_tdys_menu/', views.v_tdys_menu),
    path('v_tdys_menu_post/', views.v_tdys_menu_post),
    path('r_change_pswd/', views.r_change_pswd),
    path('v_bill_tbl_details/', views.v_bill_tbl_details),
    path('v_profile/', views.v_profile),
    path('admin_home', views.admin_home),
    path('r_home/', views.r_home),

    # ------Android------------------------------------------------------

    path('and_login_post/', views.and_login_post),
    path('and_add_rating_post/', views.and_add_rating_post),
    path('and_add_complaint_post/', views.and_add_complaint_post),
    path('and_add_feedback_post/', views.and_add_feedback_post),
    path('and_add_hlp_rqst/', views.and_add_hlp_rqst),
    path('Order_food/', views.Order_food),
    path('and_v_reply/', views.and_v_reply),
    path('and_v_tdy_menu/', views.and_v_tdy_menu),
    path('and_Cust_v_tdy_spcl/', views.and_Cust_v_tdy_spcl),
    path('and_v_ordr_status/', views.and_v_ordr_status),
    path('and_v_bill/', views.and_v_bill),
    path('and_v_toplist/', views.and_v_toplist),
    path('and_Cust_v_assin_order/', views.and_Cust_v_assin_order),

    # -----------------kitchen--------------------------

    path('and_K_v_order/', views.and_K_v_order),
    path('and_k_add_odr_sts/', views.and_k_add_odr_sts),

    # ------------------srvstn--------------------------

    path('and_srvStn_v_help_rqst/', views.and_srvStn_v_help_rqst),
    path('and_srvStn_v_all_ordr_status/', views.and_srvStn_v_all_ordr_status),
    path('and_srvStn_asign_order/', views.and_srvStn_asign_order),
    path('and_srvStn_v_assin_order/', views.and_srvStn_v_assin_order),
    path('and_srvStn_add_tdy_spcl/', views.and_srvStn_add_tdy_spcl),
    path('and_Srvstn_v_tdys_spcl/', views.and_Srvstn_v_tdys_spcl),

]
