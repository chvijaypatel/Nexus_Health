from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(models.Model):
    
    title = models.CharField(max_length=255, unique=True)
    blogs_img=models.ImageField(upload_to='Blog/Blog_Img')
    uper_content = RichTextField()
    middle_content = RichTextField()
    content_img =models.ImageField(upload_to='Blog/Content_Img')
    lower_content = RichTextField()

    slug = models.SlugField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-publish_date"]
    
    def get_date(self):
        time = datetime.now()
        if self.publish_date.day == time.day:
            return str(time.hour - self.publish_date.hour) + " hours ago"
        else:
            if self.publish_date.month == time.month:
                return str(time.day - self.publish_date.day) + " days ago"
            else:
                if self.publish_date.year == time.year:
                    return str(time.month - self.publish_date.month) + " months ago"
        return self.publish_date

    def __str__(self):
        return self.title

    

# Models for <--Blog -->Blog
class Blog_Page(models.Model):
    page_name = models.CharField(max_length=200)
    header_image=models.ImageField(upload_to='Header/Blog_Page_Img')

    def __str__(self):
        return self.page_name   

class Tags_Line_Content(models.Model):
      blog_page=models.ForeignKey(Blog_Page,on_delete=models.CASCADE)
      tags_content = models.CharField(max_length=400)        

# comment model 
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    phoneno=models.CharField(max_length=10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    
    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)
    
    def __str__(self):
        return 'Comment: {} -by: {}'.format(self.message, self.name)



class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='reply', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    phoneno=models.CharField(max_length=10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Reply: {} -by: {}'.format(self.message, self.name)+ " : " +str(self.comment)

