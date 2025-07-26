from django.shortcuts import render
from blog_pages.models import post

def blog_view(request):
    posts = post.objects.all()
    context = {'posts' : posts}
    return render(request, 'blog-home.html',context)

def blog_single(request):
    return render(request, 'blog-single.html')

def test(request):
    posts = post.objects.all()
    context = {'posts' : posts}
    return render(request, 'test.html', context)
