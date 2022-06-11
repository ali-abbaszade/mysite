from django.urls import reverse
from xml.etree.ElementTree import Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages


def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=now)
    
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])

    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])

    posts = Paginator(posts, 4)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)       

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your comment submited successfully")
        else:
            messages.add_message(request, messages.ERROR, "Your comment didnt submited")


    post = get_object_or_404(Post, pk=pid, status=1)
    if not post.login_require:
        comments = Comment.objects.filter(post=post.id, approved=True).order_by("-created_date")

        next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
        prev_post = Post.objects.filter(id__lt=post.id).order_by('id').last()

        post.counted_views = post.counted_views + 1

        form = CommentForm()

        context = {'post': post, 'next_post':next_post, 'prev_post':prev_post, 'comments':comments, 'form':form}
        post.save()
        return render(request, 'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

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
