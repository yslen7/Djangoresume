from django.contrib import admin
from .models import Overview, PersonalInfo
from .models import Education, Job, JobAccomplishment
from .models import Skillset, Skill, ProgrammingLanguage, Language, Achievement, Project

# Register your models here.

class OverviewAdmin(admin.ModelAdmin): #customize appearance
    list_display = ['text'] #otherwise it displays 'object'
admin.site.register(Overview,OverviewAdmin)

admin.site.register(PersonalInfo)

admin.site.register(Job)
admin.site.register(JobAccomplishment)
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

admin.site.register(Education,EducationAdmin)