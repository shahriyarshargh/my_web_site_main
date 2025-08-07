from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import StaticViewSitemap
from blog_pages.sitemaps import BlogPageSitemap
import debug_toolbar

sitemaps ={
    'static' : StaticViewSitemap,
    'blog': BlogPageSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('blog/', include('blog_pages.urls')), 
    path('sitemap.xml',sitemap,{'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', include('robots.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('summernote/', include('django_summernote.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
