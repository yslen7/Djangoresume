from django.contrib import admin
from .models import Overview, PersonalInfo, Education, Job, JobAccomplishment, Skillset, Skill
# Register your models here.
admin.site.register(Overview)
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Job)
admin.site.register(JobAccomplishment)
admin.site.register(Skillset)
admin.site.register(Skill)