from django.urls import include, path
from blog_pages.views import *


app_name = "blog"
urlpatterns = [
    path('', blog_view, name='blog-home'),
    path("<int:pid>" ,blog_single, name='single'),
    path('search/',blog_search,name='search'),
    path('tag/<str:tag_name>' , blog_view, name='tag'),
    
]
