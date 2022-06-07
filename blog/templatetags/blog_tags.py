from imp import create_dynamic
from telnetlib import STATUS
from unicodedata import category
from xml.etree.ElementTree import Comment
from django import template
from blog.models import Post, Comment
from blog.models import Category

register = template.Library()

@register.simple_tag(name="totalposts")
def total_posts():
    posts = Post.objects.filter(status=1).count()
    return posts
    

@register.simple_tag(name="posts")
def total_posts():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name="comments_count")
def comment_count(pid):
    return Comment.objects.filter(post=pid, approved=True).count()


@register.filter        
def snippet(value, arg=5):
    return value[:arg] + "..."

@register.inclusion_tag('blog/blog-latest-post.html') 
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}   

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    return {'categories':cat_dict}    

@register.inclusion_tag('website/index-latest-posts.html')
def six_latest_posts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:6]

    return {'posts':posts}    
    