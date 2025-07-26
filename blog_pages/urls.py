from django.urls import path
from blog_pages.views import *

app_name = "blog"
urlpatterns = [
    path('', blog_view, name='blog-home'),
    path("blog/single" ,blog_single, name='single'),
    path("test" ,test, name='test'),
    
]
