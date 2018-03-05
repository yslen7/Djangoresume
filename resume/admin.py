from django.contrib import admin
from .models import Overview, PersonalInfo
from .models import Education, Job, JobAccomplishment
from .models import Skillset, Skill, ProgrammingLanguage, Language, Achievement, Project

# Register your models here.

class OverviewAdmin(admin.ModelAdmin): #customize appearance
    list_display = ['text'] #otherwise it displays 'object'
admin.site.register(Overview,OverviewAdmin)

admin.site.register(PersonalInfo)


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
    ordering = ['-job__end_date','order']
    def get_job(self, obj):
        return obj.job.company
    get_job.short_description = 'Job'
    get_job.admin_order_field = 'job__end_date'

class SkillsetAdmin(admin.ModelAdmin):
    exclude = ()
    list_filter = ('name',)
    search_fields = ('name',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'end_date'
    ordering = ['name', 'id']

class SkillAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('get_skillset','order', 'name', 'id')
    list_filter = ('skillset__name', 'name', 'id')
    search_fields = ('skillset__name',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['skillset__name','order']
    def get_skillset(self, obj):
        return obj.skillset.name
    get_skillset.short_description = 'skillset'
    get_skillset.admin_order_field = 'skillset__name'

class AchievementAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('description', 'order', 'url','id')
    list_filter = ('description', 'order', 'url','id')
    search_fields = ('description','name',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['order','id']

class ProgrammingLanguageAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('name', 'order', 'level',)
    list_filter = ('name','level', 'description', 'order')
    search_fields = ('name','level', 'description', 'order',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['order','name']

class LanguageAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('language', 'level',)
    list_filter = ('language', 'level',)
    search_fields = ('language', 'level',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['-level','language']

class ProjectAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('name','order', 'description',)
    list_filter = ('name','order', 'description',)
    search_fields = ('name','order', 'description', 'link',)
    #prepopulated_fields = {'slug': ('degree',)}
    #date_hierarchy = 'order'
    ordering = ['order','name']


admin.site.register(Education, EducationAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobAccomplishment, JobAccomplishmentAdmin)
admin.site.register(Skillset, SkillsetAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Achievement, AchievementAdmin)

admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Project, ProjectAdmin)
