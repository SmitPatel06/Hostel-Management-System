from django.urls import path,include
from django.conf.urls import url
from django.urls import path



from . import views

app_name = 'accounts'

urlpatterns = [
   # path('', views.index, name='index'),
    
    
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("adminlogin",views.adminlogin,name="adminlogin"),
    path("logout",views.logout,name="logout"),
    path('mainpage',views.mainpage,name='mainpage'),
    path('admin',views.admin,name='admin'),
    path('adminback',views.adminback,name='adminback'),
    #path('adminmain',views.adminmain,name='adminmain'),
    path('student',views.student,name='student'),
    path('apply',views.apply,name='apply'),
    path("notice",views.notice,name="notice"),
    path('addnotice',views.addnotice,name='addnotice'),
    path("getnotice",views.getnotice,name="getnotice"),
    path('addstudent',views.addstudent,name='addstudent'),
    path('getstudentdetails',views.getstudentdetails,name='getstudentdetails'),
    path('deleterecord/<int:id>',views.deleterecord,name='deleterecord'),
    path('addpayment',views.addpayment,name='addpayment'),
    path('payment',views.payment,name='payment'),
    #url(r'^addnotice/$',views.addnotice),
   
    path('getpaymentdetails',views.getpaymentdetails,name='getpaymentdetails'),
    path('addroom',views.addroom,name='addroom'),
    path('addrooms',views.addrooms,name='addrooms'),
    path('getroomdetails',views.getroomdetails,name='getroomdetails'), 

] 