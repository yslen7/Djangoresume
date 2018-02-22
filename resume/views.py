from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.template import RequestContext

from .models import Overview, PersonalInfo, Education, Job, Accomplishment, Skillset, Skill



from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



def index(request):
    site_name = RequestSite(request).domain
    personal_info = PersonalInfo.objects.all()[:1]
    overview = Overview.objects.all()[:1]
    education = Education.objects.all()
    job_list = Job.objects.all()
    skill_sets = Skillset.objects.all()

    return render(request, 'resume/resume.html', {
        'site_name': site_name,
        'personal_info': personal_info,
        'overview' : overview,
        'job_list' : job_list,
        'education' : education,
        'skill_sets' : skill_sets,
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