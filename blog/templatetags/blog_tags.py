from imp import create_dynamic
from telnetlib import STATUS
from unicodedata import category
from django import template
from blog.models import Post
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

@register.filter        
def snippet(value, arg=5):
    return value[:arg] + "..."

@register.inclusion_tag('blog/blog-papular-post.html') 
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}   

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    return {'categories':cat_dict}    