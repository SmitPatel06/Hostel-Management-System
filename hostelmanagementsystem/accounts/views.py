from django.template.loader import get_template




from django.shortcuts import render,redirect
# from django.shortcuts import render_to_response
from django.contrib.auth.models import User,auth
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.context_processors import csrf
from accounts.models import Notice
from accounts.models import Student
from accounts.models import Payment
from accounts.models import Addstudent

from django.views import generic
from django.views.generic import ListView

# Create your views here.

class StudentListView(generic.ListView):
	model = Notice

class PaymentListView(ListView):
    model=Payment
    template_name='accounts/main.html'

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user= auth.authenticate(username=username,password=password)

        if  user is not None:
            auth.login(request,user)
            return render(request,'mainpage.html')
        
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
            
        
    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
        else:
            messages.info(request,'password does not match...')
            return redirect('register')
        return render(None,'login.html')



    else:
        return render(request,'register.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user= auth.authenticate(username=username,password=password)

        if  user is not None:
            auth.login(request,user)
            return render(None,'admin.html')
        
        else:
            messages.info(request,'invalid credentials')
            return render(None,'adminlogin.html')
        
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def mainpage(request):
    return render(None,'mainpage.html')

def admin(request):
    return render(None,'adminlogin.html')

def student(request):
    return render(None,'student.html')

def adminback(request):
    return render(None,'admin.html')
    

        
    

def adminmain(request):
    return render(None,'adminmain.html')
def apply(request):
    return render(None,'addstudent.html')

def notice(request):
    return render(None,'notice.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def addnotice(request):
    nts=request.POST.get('notice', '')
    decr=request.POST.get('description', '')
    s=Notice(notice_title=nts,description_data=decr)
    s.save()
    return render(None,'notice.html')

def getnotice(request):
    all_notice=Notice.objects.all()
    return render(request,"getnotice.html",{'Notices':all_notice})


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def addstudent(request):
    s_name=request.POST.get('studentname','')
    fname=request.POST.get('fathername','')
    bdate=request.POST.get('birthdate','')
    sgen=request.POST.get('gender','')
    mno=request.POST.get('mobileno','')
    sbranch=request.POST.get('branch','')
    sage=request.POST.get('age','')
    sarea=request.POST.get('area','')
    scity=request.POST.get('city','')
    sstate=request.POST.get('state','')
    semail=request.POST.get('email','')
    ssemester=request.POST.get('semester','')
    std=Student(student_name=s_name,f_name=fname,b_date=bdate,s_gender=sgen,mobile_no=mno,branch=sbranch,s_age=sage,add_area=sarea,add_city=scity,add_state=sstate,s_email=semail,s_sem=ssemester)

    std.save()
    return render(None,'addstudent.html')


def getstudentdetails(request):
    all_data=Student.objects.all()
    return render(request,"getdetails.html",{'Student':all_data})
    

def deleterecord(request,id):
    st=Student.objects.get(id=id)
    st.delete()
    return render(request,'admin.html')


def payment(request):
    return render(None,'payment.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def addpayment(request):
    s_year=request.POST.get('year','')
    s_amount=request.POST.get('amount','')
    s_paytype=request.POST.get('paytype','')
    s_paydetails=request.POST.get('paydetails','')
    s_room=request.POST.get('roomno','')
    s_paymentdate=request.POST.get('paymentdate','')

    pay=Payment(p_year=s_year,p_amount=s_amount,p_type=s_paytype,p_details=s_paydetails,p_roomno=s_room,created_date=s_paymentdate)
    pay.save()
    return render(None,'payment.html')


def getpaymentdetails(request):
    all_payment=Payment.objects.all()
    return render(request,"getpayment.html",{'Payments':all_payment})






from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def addroom(request):
    st_name=request.POST.get('name','')
    st_lastnane=request.POST.get('lname','')
    st_sem=request.POST.get('sem','')
    st_branch=request.POST.get('branch','')
    st_roomno=request.POST.get('roomno','')

    room=Addstudent(s_name=st_name,s_surname=st_lastnane,s_sem=st_sem,s_branch=st_branch,s_room=st_roomno)
    room.save()
    return render(None,'addroom.html')

def addrooms(request):
    return render(None,'addroom.html')

def getroomdetails(request):
    all_room=Addstudent.objects.all()
    return render(request,"roomdetail.html",{'Addroom':all_room})