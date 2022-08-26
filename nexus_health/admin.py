from django.contrib import admin
from .models import *
# Register your models here.


class About_ParagrapInline(admin.TabularInline):
    model = About_Paragrap

class Mission_tagsInline(admin.TabularInline):
    model = Mission_tags

class Care_Provider_TeamInline(admin.TabularInline):
    model = Care_Provider_Team

class About_Us_Page_Admin(admin.ModelAdmin):
    inlines = [About_ParagrapInline,Mission_tagsInline,Care_Provider_TeamInline]
    # list_display = ('product_name','categories','section')
    # list_editable= ('categories','section')

class Resources_DetailInline(admin.TabularInline):
    model = Resources_Detail

class Resources_Page_Admin(admin.ModelAdmin):
    inlines = [Resources_DetailInline,]

class Our_Partners_ImgInline(admin.TabularInline):
    model = Our_Partners_Img

class Our_PartnersInline(admin.TabularInline):
    model = Our_Partners

class Partners_Page_Admin(admin.ModelAdmin):
    inlines = [Our_Partners_ImgInline,Our_PartnersInline]

class All_DepartmentsInline(admin.TabularInline):
    model = All_Departments

class Job_PostInline(admin.TabularInline):
    model = Job_Post

class Careers_Page_Admin(admin.ModelAdmin):
    inlines = [All_DepartmentsInline,Job_PostInline]


class Contact_DetailsInline(admin.TabularInline):
    model = Contact_Details

class Contact_Page_Admin(admin.ModelAdmin):
    inlines = [Contact_DetailsInline,]


admin.site.register(HomeBanner1)
admin.site.register(Services_Department)
admin.site.register(Services_Department_Card)
admin.site.register(GP_Services_Feedback)
admin.site.register(Video_Section)
admin.site.register(Fun_Facts)
admin.site.register(Patient_Testimonial)
admin.site.register(Opening_Hours)
admin.site.register(Join_Our_Team)
admin.site.register(About_Us_Page,About_Us_Page_Admin)
# admin.site.register(About_Paragrap)
# admin.site.register(Mission_tags)
admin.site.register(Care_Provider_Team)
admin.site.register(Appointment_Page)
admin.site.register(Careers_Page,Careers_Page_Admin)
admin.site.register(All_Departments)
admin.site.register(Job_Post)
admin.site.register(Job_Application_Forms)
admin.site.register(Resources_Page,Resources_Page_Admin)
admin.site.register(Partners_Page,Partners_Page_Admin)
# admin.site.register(Our_Partners_Img)
# admin.site.register(Our_Partners)
admin.site.register(Contact_Page,Contact_Page_Admin)
admin.site.register(Contact_Now)
admin.site.register(Contact_Details)
admin.site.register(Appointment)

admin.site.site_header="NEXUS-HEALTH ADMIN"
admin.site.site_title="Nexus-Health Admin Panel"
admin.site.index_title="Nexus-Health Admin Panel"







