from django.contrib import admin
from .models import Overview, PersonalInfo
from .models import Education, Job, JobAccomplishment
from .models import Skillset, Skill, ProgrammingLanguage, Language, Achievement, Project

# Register your models here.
admin.site.register(Overview)
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Job)
admin.site.register(JobAccomplishment)
admin.site.register(Skillset)
admin.site.register(Skill)
admin.site.register(ProgrammingLanguage)
admin.site.register(Language)
admin.site.register(Achievement)
admin.site.register(Project)