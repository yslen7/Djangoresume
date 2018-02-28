from django.db import models 
import time

class Overview(models.Model):
    text = models.TextField()
    class Meta:
        verbose_name_plural = "Overview"
    def __unicode__(self):
        return self.text[0:40] + '...'

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, help_text="e.g. city such as Boston")
    region = models.CharField(max_length=255, help_text="e.g. MA or Italy",blank=True)
    title = models.CharField(max_length=255, help_text="e.g. Developer",blank=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    site = models.URLField(blank=True)
    sitename  = models.CharField(max_length=255, default = site)
    twittername = models.CharField(max_length=100, blank=True)
    class Meta:
        verbose_name_plural = "Personal Info"    
    def full_name(self):
        return " ".join([self.first_name, self.middle_name, self.last_name])    
    def githubname(self):
        print('git='+str(self.github))
        if self.github is not '':
            return self.github.rsplit('/',maxsplit=1)[1]
        else:
            return None
    def __unicode__(self):
        return self.full_name()

class Language(models.Model):
    language = models.CharField(max_length=20,blank=False)
    level = models.CharField(max_length=30,blank=False)
    #personalinfo = models.ForeignKey('PersonalInfo',on_delete=models.CASCADE)
    ordering = models.IntegerField(default=1)
    class Meta:
        ordering = ['ordering','id']
    def __unicode__(self):
        return ''.join([self.PersonalInfo.full_name, '-', self.language, '-', self.level])

class Education(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    school_url = models.URLField('School URL', blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    #is_current = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Education"
    def edu_date_range(self):
        return ''.join(['(', self.formatted_start_date(), 
            '-', self.formatted_end_date(), ')'])
    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")
    def full_end_date(self):
        if (self.end_date == None):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.end_date.strftime("%Y-%m-%d")
    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")
    def formatted_end_date(self):
        if (self.end_date == None):
            return "Current"
        else:
            return self.end_date.strftime("%b %Y")
    def __unicode__(self):
        return ' '.join([self.name, self.edu_date_range()])


class Job(models.Model):
    company = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    company_url = models.URLField('Company URL')
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    is_current = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    company_image = models.CharField(max_length=250, blank=True, 
        help_text='path to company image, local or otherwise')
    class Meta:
        db_table = 'jobs'
        ordering = ['-end_date','-start_date']        
    def job_date_range(self):
        return ''.join(['(', self.formatted_start_date(),'-', 
            self.formatted_end_date(), ')'])    
    def full_start_date(self):
        if self.start_date is None:
            return None
        return self.start_date.strftime("%Y-%m-%d")
    def full_end_date(self):
        if (self.is_current is True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.end_date.strftime("%Y-%m-%d")
    def formatted_start_date(self):
        if self.start_date is None:
            return None
        return self.start_date.strftime("%b %Y")        
    def formatted_end_date(self):
        if self.is_current == True or self.end_date is None:
            return "Current"
        else:
            return self.end_date.strftime("%b %Y")
    def __unicode__(self):
        return ' '.join([self.company, self.job_date_range()])

class Accomplishment(models.Model):
    description = models.TextField()
    #job = models.ForeignKey(Job)
    job = models.ForeignKey('Job',on_delete=models.CASCADE)
    order = models.IntegerField(default=1)
    class Meta:
        db_table = 'accomplishments'
        ordering = ['order', 'id']
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
