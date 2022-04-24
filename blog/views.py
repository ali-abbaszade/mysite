from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=now)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    post.counted_views = post.counted_views + 1
    context = {'post': post}
    post.save()
    return render(request, 'blog/blog-single.html', context)


def test(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    post.counted_views = post.counted_views + 1
    post.save()
    context = {'post': post}
    return render(request, 'test.html', context)
