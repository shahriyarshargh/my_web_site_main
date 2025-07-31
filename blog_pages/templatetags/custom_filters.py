from django import template
from blog_pages.models import Post

register = template.Library()

@register.filter(name='word_excerpt')
def word_excerpt(value, arg):
    try:
        arg = int(arg)
        words = value.split()
        if len(words) <= arg:
            return value
        return ' '.join(words[:arg]) + '...'
    except:
        return value

@register.inclusion_tag('latestposts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('latest-posts.html')
def show_latest_posts():
    posts = Post.objects.order_by('-published_date')[:6]
    return {'latest_posts': posts}