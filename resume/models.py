from django.db import models 
import time


'''
from resume.models import Overview
over=Overview.objects.create(text='This is a test overview for this CV')
from resume.models import 

from resume.models import PersonalInfo
pi=PersonalInfo.objects.create('email': 'AlessandroMarin80@gmail.com', 'region': 'Massachusetts', 'region_shorthand': 'MA', 'first_name': 'Alessandro', 'locality': 'Boston', 'last_name': 'Marin')
pi.linkedin='https://www.linkedin.com/in/alessandromarin80/'
pi.save()

from resume.models import Education
sks=Skillset.objects.create(name='Programming Languages')
sks.save()
s1=Skill.objects.create(name='Python',skillset=sks)
s2=Skill.objects.create(name='Django',skillset=sks)


date=datetime.date(year=2018,month=2,day=19)
date2=datetime.date(year=2018,month=2,day=20)
j=Job.objects.create(company='MyCompany',start_date=date,completion_date=date2)
j.company='my company'
j.company_url='www.google.com'
j.__dict__

from resume.models import Education
Education.objects.create(name='University Somewhere',start_date=date,completion_date=date2)

'''

class Overview(models.Model):
    text = models.TextField()
    class Meta:
        verbose_name_plural = "Overview"
    def __unicode__(self):
        return self.text[0:40] + '...'

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, help_text="e.g. city such as Boston")
    region = models.CharField(max_length=255, help_text="e.g. state such as Massachusetts")
    region_shorthand = models.CharField(max_length=64, help_text="e.g. shorthand (abbr), MA for Massachusetts")
    email = models.EmailField()
    linkedin = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = "Personal Info"
    
    def full_name(self):
        return " ".join([self.first_name, self.last_name])
    
    def __unicode__(self):
        return self.full_name()

class Education(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    school_url = models.URLField('School URL')
    start_date = models.DateField()
    completion_date = models.DateField()
    summary = models.TextField()
    is_current = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Education"

    def edu_date_range(self):
        return ''.join(['(', self.formatted_start_date(), 
            '-', self.formatted_end_date(), ')'])

    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.completion_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.completion_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.name, self.edu_date_range()])


class Job(models.Model):
    company = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    company_url = models.URLField('Company URL')
    description = models.TextField(blank=True)
    start_date = models.DateField()
    completion_date = models.DateField()
    is_current = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    company_image = models.CharField(max_length=250, blank=True, 
        help_text='path to company image, local or otherwise')

    class Meta:
        db_table = 'jobs'
        ordering = ['-completion_date','-start_date']
        
    def job_date_range(self):
        return ''.join(['(', self.formatted_start_date(),'-', 
            self.formatted_end_date(), ')'])
    
    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.completion_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
            return self.start_date.strftime("%b %Y")
        
    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.completion_date.strftime("%b %Y")

    def __unicode__(self):
        return ' '.join([self.company, self.job_date_range()])

class Accomplishment(models.Model):
    description = models.TextField()
    #job = models.ForeignKey(Job)
    job = models.ForeignKey('Job',on_delete=models.CASCADE)
    

    order = models.IntegerField()

    class Meta:
        db_table = 'accomplishments'
        ordering = ['order']

    def __unicode__(self):
        return ''.join([self.job.company, '-', self.description[0:50], '...'])

class Skillset(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name =  models.CharField(max_length=250)
    skill_url = models.URLField('Skill URL', blank=True)
    skillset = models.ForeignKey('Skillset',on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return ''.join([self.skillset.name, '-', self.name])
