# blog_pages/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_view(request):
    posts = Post.objects.filter(status=True).order_by('created_date')
    return render(request, 'blog-home.html', { 'posts': posts })


def blog_single(request, pid):
    
    post = get_object_or_404(Post, pk=pid, status=True)

    
    all_posts = list(
        Post.objects
            .filter(status=True)
            .order_by('created_date')
    )

    
    try:
        idx = all_posts.index(post)
    except ValueError:
        idx = None

    
    prev_post = all_posts[idx - 1] if idx is not None and idx > 0 else None
    next_post = all_posts[idx + 1] if idx is not None and idx < len(all_posts) - 1 else None

    
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog-single.html', context)


def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    return render(request, 'test.html', { 'post': post })