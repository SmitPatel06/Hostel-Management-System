from django.contrib import admin

# Register your models here.
from accounts.models import Student
from accounts.models import Notice
from accounts.models import Payment
from accounts.models import Addstudent
admin.site.register(Student)
admin.site.register(Notice)
admin.site.register(Payment)
admin.site.register(Addstudent)