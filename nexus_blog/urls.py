from django.urls import path
from . import views

urlpatterns = [  
     
   
    path('blog', views.PostList, name='blog'),
    # path('blog', views.PostList.as_view(), name='blog'),
    # path('blog/<slug:slug>', views.PostDetail.as_view(), name='post_detail'), 
    path('blog/<slug:slug>', views.PostDetail, name='post_detail'), 
    path('blog/<int:post_id>/<int:comment_id>/', views.reply, name='reply'),

     
]