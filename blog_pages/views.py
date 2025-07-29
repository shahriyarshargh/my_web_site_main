# blog_pages/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_view(request):
    posts = Post.objects.filter(status=True).order_by('created_date')
    return render(request, 'blog-home.html', { 'posts': posts })


def blog_single(request, pid):
    # ۱. واکشیِ پست جاری
    post = get_object_or_404(Post, pk=pid, status=True)

    # ۲. واکشی لیست مرتب از همه پست‌های فعال
    all_posts = list(
        Post.objects
            .filter(status=True)
            .order_by('created_date')
    )

    # ۳. پیدا کردن اندیس پست جاری
    try:
        idx = all_posts.index(post)
    except ValueError:
        idx = None

    # ۴. تعیین پست قبلی و بعدی (در صورت وجود)
    prev_post = all_posts[idx - 1] if idx is not None and idx > 0 else None
    next_post = all_posts[idx + 1] if idx is not None and idx < len(all_posts) - 1 else None

    # ۵. ارسال به قالب
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog-single.html', context)


def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    return render(request, 'test.html', { 'post': post })