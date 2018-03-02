from django.contrib import admin
from .models import Overview, PersonalInfo, Education, Job, Accomplishment, Skillset, Skill
# Register your models here.
admin.site.register(Overview)
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Job)
admin.site.register(Accomplishment)
admin.site.register(Skillset)
admin.site.register(Skill)