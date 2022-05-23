from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone



def blog_view(request, cat_name=None):
    now = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=now)
    
    if cat_name:
        posts = Post.objects.filter(category__name=cat_name)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)

    single = Post.objects.get(id=pid)
    next_post = Post.objects.filter(id__gt=single.id).order_by('id').first()
    prev_post = Post.objects.filter(id__lt=single.id).order_by('id').last()

    post.counted_views = post.counted_views + 1

    context = {'post': post, 'single' : single, 'next_post':next_post, 'prev_post':prev_post}
    post.save()
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = Post.objects.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def test(request):
    return render(request, 'test.html')
