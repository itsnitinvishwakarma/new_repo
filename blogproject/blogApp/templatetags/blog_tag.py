from django import template
from blogApp.models import Post
register=template.Library()

@register.simple_tag(name='mytag')
def total_posts():
    post=Post.objects.count()
    return post

@register.inclusion_tag('latestpost.html',name='mytag2')
def show_latest_posts(count=2):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

#from django.db.models import Count
'''@register.assignment_tag
def get_most_commented_posts(count=4):
    most_commented_posts=Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return most_commented_posts
'''