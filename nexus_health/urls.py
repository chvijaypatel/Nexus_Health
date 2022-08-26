from django.urls import path
from . import views

urlpatterns = [  
     
     path('base/', views.base, name='base'),
     path('', views.home, name='home'),
     path('about_us', views.about_us, name='about_us'),
     path('contact', views.contact, name='contact'),
     path('404', views.error404, name='404'),
     path('appointment', views.appointment, name='appointment'),
     path('careers', views.careers, name='careers'),
     path('careers/<slug:slug>', views.JobDetail, name='job_detail'), 
     path('lowerbackpain', views.lowerbackpain, name='lowerbackpain'),
     path('occupational_health', views.occupational_health, name='occupational_health'),
     path('partners', views.partners, name='partners'),
     path('patientinformation', views.patientinformation, name='patientinformation'),
     path('resources', views.resources, name='resources'),
     path('working_with_nhs', views.working_with_nhs, name='working_with_nhs'),
     path('services_feedback', views.services_feedback, name='services_feedback'),
     path('patient_feedback', views.patient_feedback, name='patient_feedback'),

]