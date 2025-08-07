# blog_pages/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def blog_view(request):
    post_list = Post.objects.filter(status=True).order_by('created_date')
    paginator = Paginator(post_list, 3)  # 3 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 'posts': page_obj }
    return render(request, 'blog-home.html', context)
    if kwargs.get('tag_name') != None:
        posts = posts.filter( tag__name__in=[kwargs['tag_name']])
    


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



    


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
       if s := request.GET.get('s'):
           posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts':posts}
    return render(request, 'blog-home.html',context)
