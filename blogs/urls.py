from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('addblog/',views.addblog,name='addblog'),
    path('<int:blog_id>/',views.viewblog,name='viewblog'),

    
]