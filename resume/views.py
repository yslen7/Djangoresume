from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext

from .models import Overview, PersonalInfo
from .models import Education, Job, JobAccomplishment, Publication
from .models import Skillset, Skill, ProgrammingLanguage, Language, Achievement, Project



from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



def index(request):
    site_name = RequestSite(request).domain
    personal_info = PersonalInfo.objects.all()[:1]
    overview = Overview.objects.all()[:1]
    education = Education.objects.all()
    jobaccomplishment = JobAccomplishment.objects.all()
    achievement = Achievement.objects.all()
    job_list = Job.objects.all()
    skillset = Skillset.objects.all()
    proglan = ProgrammingLanguage.objects.all()
    language = Language.objects.all()
    project = Project.objects.all()
    publication = Publication.objects.all()

    return render(request, 'resume/resume.html', {
        'site_name': site_name,
        'personal_info': personal_info,
        'overview' : overview,
        'education' : education,
        'language' : language,
        'achievement' : achievement,
        'job_list' : job_list,        
        'skillset' : skillset,
        'proglan' : proglan,
        'project' : project,
        'publication' : publication,
    })


class OverviewCreate(CreateView):
    model = Overview
    fields = '__all__'
    initial={'text':'add an overview of your resume',}
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class OverviewUpdate(UpdateView):
    model = Overview
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class OverviewDelete(DeleteView):
    model = Overview
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')

class PersonalInfoCreate(CreateView):
    model = PersonalInfo
    fields = '__all__'
    initial={'text':'add personal info to your resume',}
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class PersonalInfoUpdate(UpdateView):
    model = PersonalInfo
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class PersonalInfoDelete(DeleteView):
    model = PersonalInfo
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class EducationCreate(CreateView):
    model = Education
    fields = '__all__'
    initial={'text':'add education to your resume',}
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class EducationUpdate(UpdateView):
    model = Education
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class EducationDelete(DeleteView):
    model = Education
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
'''
class Language(CreateView):
    model = Language
    fields = '__all__'
    initial={'text':'add a language to your skills',}
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class LanguageUpdate(UpdateView):
    model = Language
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class LanguageDelete(DeleteView):
    model = Language
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class Achievement(CreateView):
    model = Achievement
    fields = '__all__'
    initial={'text':'add an achievement to your resume',}
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class AchievementUpdate(UpdateView):
    model = Achievement
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class AchievementDelete(DeleteView):
    model = Achievement
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class ProgrammingLanguage(CreateView):
    model = ProgrammingLanguage
    fields = '__all__'
    initial={'text':'add a programming language',}
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class ProgrammingLanguageUpdate(UpdateView):
    model = ProgrammingLanguage
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class ProgrammingLanguageDelete(DeleteView):
    model = ProgrammingLanguage
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class Project(CreateView):
    model = Project
    fields = '__all__'
    initial={'text':'add a project',}
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class ProjectUpdate(UpdateView):
    model = ProgrammingLanguage
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class ProjectDelete(DeleteView):
    model = ProgrammingLanguage
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
'''