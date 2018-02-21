"""djangoresume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from resume import views #import my views
from django.urls import path
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='resume_home'),
]
### TODO <int:pk> can be a slug - https://chriskief.com/2012/12/29/django-generic-detailview-without-a-pk-or-slug/
urlpatterns += [  
    path('overview/create/', views.OverviewCreate.as_view(), name='overview_create'),
    path('overview/update/', views.OverviewUpdate.as_view(), name='overview_update'),
    path('overview/<int:pk>/delete/', views.OverviewDelete.as_view(), name='overview_delete'),
]
