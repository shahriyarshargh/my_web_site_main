from django.urls import path, re_path
from .views import coming_soon

urlpatterns = [
    path('', coming_soon),
    re_path(r'^.*$', coming_soon),  # Catch-all
]
