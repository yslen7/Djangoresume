from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext

from .models import Overview, PersonalInfo, Education, Job, JobAccomplishment, Skillset, Skill, Language, Achievement, ProgrammingLanguage



from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



def index(request):
    site_name = RequestSite(request).domain
    personal_info = PersonalInfo.objects.all()[:1]
    overview = Overview.objects.all()[:1]
    education = Education.objects.all()
    jobaccomplishment = JobAccomplishment.objects.all()
    hey=Achievement.__dict__
    print(Achievement.__dict__)
    achievement = Achievement.objects.all()
    job_list = Job.objects.all()
    skillset = Skillset.objects.all()
    proglan = ProgrammingLanguage.objects.all()
    language = Language.objects.all()

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

class Languages(CreateView):
    model = Language
    fields = '__all__'
    initial={'text':'add a language to your skills',}
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class LanguagesUpdate(UpdateView):
    model = Language
    fields = '__all__'
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
class LanguagesDelete(DeleteView):
    model = Language
    template_name = 'resume/template_form.html'
    success_url = reverse_lazy('index')
'''class Achievement(CreateView):
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
'''