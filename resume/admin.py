from django.contrib import admin
from .models import Overview, PersonalInfo
from .models import Education, Job, JobAccomplishment
from .models import Skillset, Skill, ProgrammingLanguage, Language, Achievement, Project

# Register your models here.

class OverviewAdmin(admin.ModelAdmin): #customize appearance
    list_display = ['text'] #otherwise it displays 'object'
admin.site.register(Overview,OverviewAdmin)

admin.site.register(PersonalInfo)



admin.site.register(Skillset)
admin.site.register(Skill)
admin.site.register(ProgrammingLanguage)
admin.site.register(Language)
admin.site.register(Achievement)
admin.site.register(Project)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree', 'formatted_end_date', 'location', 'description')
    list_filter = ('name', 'degree', 'location')
    search_fields = ('name', 'degree')
    #prepopulated_fields = {'slug': ('degree',)}
    date_hierarchy = 'end_date'
    ordering = ['end_date', 'id']

class JobAdmin(admin.ModelAdmin):
    list_display = ('company', 'location', 'title', 'end_date')
    list_filter = ('company', 'location', 'title', 'end_date')
    search_fields = ('company', 'location', 'title')
    #prepopulated_fields = {'slug': ('degree',)}
    date_hierarchy = 'end_date'
    ordering = ['end_date', 'id']

class JobAccomplishmentAdmin(admin.ModelAdmin):
    list_display = ('get_job', 'order', 'description')
    list_filter = ('job__company', 'order')
    #search_fields = ('order')
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['-job__end_date','order'] #TODO get_job does not work
    def get_job(self, obj):
        return obj.job.company
    get_job.short_description = 'Job'
    get_job.admin_order_field = 'job__end_date'

admin.site.register(Education, EducationAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobAccomplishment, JobAccomplishmentAdmin)