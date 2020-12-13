from django.db import models

# Create your models here.

'''
django model field :-
     - html widget
     - validation 
     - db size 
'''

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Prt Time','Prt Time'),
)

class Job(models.Model): # table --> الموديل تكافئ جدول في الداتا بيس 
    title = models.CharField(max_length=100) # معناتها انه تم انشاء عمود في الداتا بيس 
    #location = 
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    #category = 
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    