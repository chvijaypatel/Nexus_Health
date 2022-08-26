from multiprocessing import context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from nexus_blog.models import Blog
from nexus_health.models import *
 
# Create your views here.
def base(request):
    
    return render(request,'base.html')

def home(request): 
    homebanners1 = HomeBanner1.objects.all().order_by('-id')[0:1]
    services_department = Services_Department.objects.all().order_by('-id')[0:1]
    services_department_card = Services_Department_Card.objects.all()
    gp_services_feedback = GP_Services_Feedback.objects.all()
    video_section = Video_Section.objects.all().order_by('-id')[0:1]
    fun_facts = Fun_Facts.objects.all()
    patient_testimonial = Patient_Testimonial.objects.all()
    opening_hours = Opening_Hours.objects.all().order_by('-id')[0:1]
    posts = Blog.objects.all().order_by('-id')
    

    context={
           'homebanners1':homebanners1 ,
           'services_department':services_department,
           'services_department_card':services_department_card,
           'gp_services_feedback':gp_services_feedback,
           'video_section':video_section,
           'fun_facts':fun_facts,
           'patient_testimonial':patient_testimonial,
           'opening_hours':opening_hours,
           'post_list':posts

     }
    return render(request,'home.html',context)

def error404(request):    
    return render(request,'pages/404.html')

def about_us(request):  

    about_us_page = About_Us_Page.objects.all().all().order_by('-id')[0:1]
    about_paragrap = About_Paragrap.objects.all()
    mission_tags = Mission_tags.objects.all()
    care_provider_team = Care_Provider_Team.objects.all()
    join_our_team = Join_Our_Team.objects.all()
    
    context={
        'about_us_page':about_us_page,
        'about_paragrap':about_paragrap,
        'mission_tags':mission_tags,
        'care_provider_team':care_provider_team,
        'join_our_team':join_our_team,
    }

    return render(request,'pages/about_us.html',context)

def contact(request): 

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        message = request.POST.get('message')
       

        app = Contact_Now(
        name = name,
        email = email,
        phoneno = phoneno,
        message = message,

        )
        app.save()
        messages.success(request,'Your contact request has been submitted Successfully! ') 

    contact_page = Contact_Page.objects.all()
    contact_details= Contact_Details.objects.all()
    contact_now= Contact_Now.objects.all()
    context={
            'contact_page':contact_page,
            'contact_details':contact_details,
            'contact_now':contact_now,
    }   
    return render(request,'pages/contact.html',context)



def appointment(request):    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        message = request.POST.get('message')
        waytoreach = request.POST.get('waytoreach')
        dayofweek = request.POST.get('dayofweek')
        timeofday = request.POST.get('timeofday')

        app = Appointment(
        name = name,
        email = email,
        phoneno = phoneno,
        message = message,
        waytoreach = waytoreach,
        dayofweek = dayofweek,
        timeofday = timeofday
        )
        app.save()
        messages.success(request,'Your appointment has been booked Successfully! ')
        appointment_page = Appointment_Page.objects.all()
        context={
                'appointment_page':appointment_page,
        }
        return render(request,'pages/appointment.html',context)
    else:
        return render(request,'pages/appointment.html')
        

def careers(request):  

    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        subject = request.POST.get('subject')
        file = request.POST.get('file')
        
        app = Job_Application_Forms(
        job_title=job_title,
        name = name,
        email = email,
        phoneno = phoneno,
        subject = subject,
        file = file,
        )
        app.save()
        messages.success(request,'Your job application has been applied Successfully! ')

    careers_page = Careers_Page.objects.all()
    all_departments = All_Departments.objects.all()
    job_application_forms =Job_Application_Forms.objects.all()
    job_post = Job_Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(job_post,2)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    
    context={
            'careers_page':careers_page,
            'all_departments':all_departments,
            'job_post':job_post,
            'job_application_forms':job_application_forms,
            'jobs':jobs,
    }  
    return render(request,'pages/careers.html',context)

def JobDetail(request, slug):    
    job_post = Job_Post.objects.filter(slug=slug)
    context = {
        'job_post': job_post,
        }
    return render(request, 'pages/job_deatils.html', context)
    
def lowerbackpain(request):    
    return render(request,'pages/lowerbackpain.html')

def occupational_health(request):    
    return render(request,'pages/occupational_health.html')

def partners(request):
    partners_page = Partners_Page.objects.all()
    our_partners_img = Our_Partners_Img.objects.all()
    our_partners = Our_Partners.objects.all()
    context={
            'partners_page':partners_page,
            'our_partners_img':our_partners_img,
            'our_partners': our_partners

    }    
    return render(request,'pages/partners.html',context)

def patientinformation(request):    
    return render(request,'pages/patientinformation.html')

def resources(request):  
    resources_page = Resources_Page.objects.all()
    resources_detail = Resources_Detail.objects.all()
    context={
            'resources_page':resources_page,
            'resources_detail':resources_detail,
    }

    return render(request,'pages/resources.html',context)

def working_with_nhs(request):    
    return render(request,'pages/working_with_nhs.html')


def services_feedback(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        designation = request.POST.get('designation')
        message = request.POST.get('message')
        
        app = GP_Services_Feedback(
        customer_name = customer_name,
        designation = designation,
        message = message,
        
        )
        app.save()
        messages.success(request,'Your Feedback has been submitted Successfully! ')
    
        return render(request, 'pages/services_feedback.html')
    else:
        return render(request,'pages/services_feedback.html')

def patient_feedback(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        image = request.POST.get('image')
        message = request.POST.get('message')
        
        app = Patient_Testimonial(
        patient_name = patient_name,
        image = image,
        message = message,
        
        )
        app.save()
        messages.success(request,'Your Feedback has been submitted Successfully! ')
    
        return render(request, 'pages/patient_feedback.html')
    else:
        return render(request,'pages/patient_feedback.html')


 
 
