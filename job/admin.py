from django.contrib import admin

# Register your models here.

from .models import Job # . معناتها بأن ملف الأدمين وملف الموديل في نفس المجلد 

admin.site.register(Job)