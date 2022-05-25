from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone



def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=now)
    
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])

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

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        # print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def test(request):
    return render(request, 'test.html')
