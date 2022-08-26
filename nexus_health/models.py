from django.db import models
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# <----- Models Start home page ------> 

# Create your models here.
# Models for <--hero-section--> HomeBanners1  
class HomeBanner1(models.Model):
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=200)
    paragraph = RichTextField()
    image=models.ImageField(upload_to='HomeBanner1')
    buttontext=models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Models for <--service-section--> All Department 
class Services_Department(models.Model):
    title = models.CharField(max_length=200)
    paragraph = RichTextField()

    def __str__(self):
        return self.title

# Models for <--service-section--> All Department Cards
class Services_Department_Card(models.Model):
    department_name = models.CharField(max_length=200)
    icon_class_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.department_name

# Models for <--feedback-section--> GP Services feedback
class GP_Services_Feedback(models.Model):
    customer_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.customer_name

# Models for <--video-section--> video-section

class Video_Section(models.Model):
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='Video_Banner')
    paragraph = RichTextField()
    buttontext=models.CharField(max_length=100)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title
        
# Models for <--fun-facts-section--> fun-facts

class Fun_Facts(models.Model):
    title = models.CharField(max_length=200)
    mobileno= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bg_image=models.ImageField(upload_to='Fun_facts_Img')
    sub_title = models.CharField(max_length=500)
    paragraph = RichTextField()
    satisfied_clients_count=models.IntegerField()
    world_awards_count=models.IntegerField()

    def __str__(self):
        return self.title
        
# Models for <--Patient Testimonial--> Patient Testimonial
class Patient_Testimonial(models.Model):
    patient_name = models.CharField(max_length=200)
    image=models.ImageField(upload_to='Patient_Img')
    message = models.TextField()

    def __str__(self):
        return self.patient_name

# Models for <--Opening Hours--> Mission_Vission

class Opening_Hours(models.Model):
    title = models.CharField(max_length=200)
    paragraph = RichTextField()
    day_to_day1=models.CharField(max_length=200)
    time_to_time1=models.CharField(max_length=200)
    day_to_day2=models.CharField(max_length=200)
    time_to_time2=models.CharField(max_length=200)

    def __str__(self):
        return self.title

# <----- Models End home page ------>        

# <----- Models Start about page ------> 

# Models for <--About Us-->About Us

class About_Us_Page(models.Model):
    page_name = models.CharField(max_length=200)
    header_image=models.ImageField(upload_to='Header/About_Img')
    image1=models.ImageField(upload_to='About_Img')
    image2=models.ImageField(upload_to='About_Img')
    paragraph_Mission = RichTextField()
    paragraph_Care_Provider = RichTextField()

    def __str__(self):
        return self.page_name
         
class About_Paragrap(models.Model): 
    about_us_page=models.ForeignKey(About_Us_Page,on_delete=models.CASCADE) 
    paragraph = RichTextField()


class Mission_tags(models.Model):  
    about_us_page=models.ForeignKey(About_Us_Page,on_delete=models.CASCADE)
    tags= models.CharField(max_length=200)    
     
class Care_Provider_Team(models.Model): 
    about_us_page=models.ForeignKey(About_Us_Page,on_delete=models.CASCADE) 
    team_member_photo =models.ImageField(upload_to='About_Img/Team_Img')
    team_member_name = models.CharField(max_length=200)
    department_name = models.CharField(max_length=200)

    def __str__(self): 
        return self.team_member_name

class Join_Our_Team(models.Model):
    title =models.CharField(max_length=200)
    paragraph = RichTextField()
    link = models.CharField(max_length=200)

# <----- Models End about page ------> 


# <----- Models Start Appointment Page ------> 

# Models for <--Appointment -->appointment
class Appointment_Page(models.Model):
    page_name = models.CharField(max_length=200)
    header_image=models.ImageField(upload_to='Header/Appointment_Page_Img')

    def __str__(self):
        return self.page_name

class Appointment(models.Model):

    CHOICES = [('Phone','Phone'),('Email','Email'),]
    WEEK_CHOICES = [('Monday', 'Monday'),('Tuesday', 'Tuesday'),('Wednesday', 'Wednesday'),('Thursday', 'Thursday'),('Friday', 'Friday'),]
    TIME_CHOICES = [('Morning', 'Morning'),('Afternoon', 'Afternoon'),]

    
    name = models.CharField(max_length=200)
    email= models.EmailField()
    phoneno= models.CharField(max_length=10)
    message = models.TextField()
    waytoreach=MultiSelectField(choices=CHOICES,max_length=100)
    dayofweek=MultiSelectField(choices=WEEK_CHOICES,max_length=100)
    timeofday=MultiSelectField(choices=TIME_CHOICES,max_length=100)


    def __str__(self):
        return self.name


# <----- Models Start Careers Page ------> 

# Models for <--Careers -->Careers
class Careers_Page(models.Model):
    page_name = models.CharField(max_length=200)
    header_image=models.ImageField(upload_to='Header/Careers_Page_Img')

    def __str__(self):
        return self.page_name

class All_Departments(models.Model):
    careers_page=models.ForeignKey(Careers_Page,on_delete=models.CASCADE)
    department_name =models.CharField(max_length=400)
    link = models.CharField(max_length=200) 
    
    def __str__(self):
        return self.department_name 

class Job_Post(models.Model):
    careers_page=models.ForeignKey(Careers_Page,on_delete=models.CASCADE)
    job_title =models.CharField(max_length=400)
    department_name =models.CharField(max_length=400)
    job_description =RichTextField()
    experience =models.CharField(max_length=400)
    loaction=models.CharField(max_length=400)
    publish_date = models.DateTimeField(blank=True, null=True)
    last_date_applay= models.DateTimeField(blank=True, null=True)
    status =models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='job_post')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.job_title + " : " + self.department_name
             

class Job_Application_Forms(models.Model):
    job_title =models.ForeignKey(Job_Post, on_delete=models.CASCADE, related_name='job_post')
    name = models.CharField(max_length=200)
    email= models.EmailField()
    phoneno= models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    file = models.FileField(upload_to='careers/Job_Application_Forms')

    def __str__(self):
        return self.name + " : " + self.subject
             

# <----- Models Start Resources Page ------> 

# Models for <--Resources -->Resources 
class Resources_Page(models.Model):
    page_name = models.CharField(max_length=200)
    header_image=models.ImageField(upload_to='Header/Resources_Page_Img')
    header_title=models.CharField(max_length=200)

    def __str__(self):
        return self.page_name

class Resources_Detail(models.Model):        
    resources_page=models.ForeignKey(Resources_Page,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Resources_Img')
    title =models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    

# <----- Models Start Partners Page ------> 

# Models for <--Partners -->Careers
class Partners_Page(models.Model):
    page_name = models.CharField(max_length=200)
    header_image=models.ImageField(upload_to='Header/Partners_Page_Img')

    def __str__(self):
        return self.page_name  
class Our_Partners_Img(models.Model):
    partners_page=models.ForeignKey(Partners_Page,on_delete=models.CASCADE)
    partners_image=models.ImageField(upload_to='Header/Our_Partners_Img')

class Our_Partners(models.Model):
    partners_page=models.ForeignKey(Partners_Page,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Header/Our_Partners')
    title =models.CharField(max_length=200)
    paragraph = RichTextField()
    link = models.CharField(max_length=200)
    

# <----- Models Start Contact Page ------> 

# Models for <--Contact -->Contact
class Contact_Page(models.Model):
    page_name = models.CharField(max_length=200)
    header_image=models.ImageField(upload_to='Header/Contact_Page_Img')
    contact_now_pargraph=models.TextField()


    def __str__(self):
        return self.page_name   

class Contact_Details(models.Model):
    contact_page=models.ForeignKey(Contact_Page,on_delete=models.CASCADE)
    phoneno1= models.CharField(max_length=100)
    phoneno2= models.CharField(max_length=100)
    email1= models.EmailField()
    email2= models.EmailField()
    address_l1=models.CharField(max_length=400)
    address_l2=models.TextField()
   

class Contact_Now(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField()
    phoneno= models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name




    
    
    
    

    

