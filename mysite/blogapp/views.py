from blogapp.forms import PostForm
from django.http import HttpResponse
from django.shortcuts import render
from blogapp.models import Post, Author



def hello_world(request):
    return render(request, 'hello_world.html', {})

def blog_index(request):
    posts = Post.objects.all().order_by('-date_created')
    context = {
        "posts": posts
    }
    return render(request, "blog_index.html", context)

def blog_author(request, author):
    posts = Post.objects.filter(
        authors__author_name__contains=author
    ).order_by(
        '-date_created'
    )
    context = {
        "author": author,
        "posts": posts
    }
    return render(request, "blog_author.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title_text=form.cleaned_data["title_text"],
                description_text=form.cleaned_data["description_text"],
                post=post
            )
            post.save()
    
    authors = Author.objects.filter(post=post)
    context = {
        "post": post,
        "authors": authors,
    }

    return render(request, "blog_detail.html", context)
