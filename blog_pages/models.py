# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=600)

    def __str__(self):
        return self.name


class Post(models.Model):
    image         = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title         = models.CharField(max_length=600)
    content       = models.TextField()
    category      = models.ManyToManyField(Category)
    counted_view  = models.PositiveIntegerField(default=0)
    status        = models.BooleanField(default=False)
    published_date= models.DateTimeField(null=True)
    created_date  = models.DateTimeField(auto_now_add=True)
    updated_date  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"{self.id} – {self.title}"

    def get_previous_post(self):
        
        return Post.objects.filter(
            created_date__gt=self.created_date,
            status=True
        ).order_by('created_date').first()

    def get_next_post(self):
       
        return Post.objects.filter(
            created_date__lt=self.created_date,
            status=True
        ).order_by('-created_date').first()