from django.http import HttpResponse
from django.shortcuts import render
from blogapp.models import Post, Author
from django.utils import timezone
from django.shortcuts import redirect


def blog_index(request):
    posts = Post.objects.all().order_by('-date_created') 
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)    
    authors = Author.objects.filter(post=post)
    context = {
        "post": post,
        "authors": authors,
    }
    return render(request, "blog_detail.html", context)


def add_post(request):
    name = request.POST["name"]
    bio = request.POST["bio"]
    title = request.POST["title"]
    description = request.POST["description"]
    a = Author(author_name=name,author_bio=bio)
    a.save()
    
    post = Post(title_text=title,description_text=description,date_created=timezone.now(),author=a)
    post.save()

    response = redirect('/blogapp/')
    return response
                  
def edit_post(request,pk):
    
    post = Post.objects.get(pk=pk)
    author = Author.objects.get(post=post)
    name = request.POST["name"]
    bio = request.POST["bio"]
    title = request.POST["title"]
    description = request.POST["description"]
    
    author.author_name = name
    author.author_bio = bio
    author.save()
    
    post.title_text=title
    post.description_text=description
    post.date_created=timezone.now()
    post.author= author
    post.save()
    
    response = redirect('/blogapp/')
    return response

def delete_post(request,pk):
     post = Post.objects.get(pk=pk)
     post.delete()
    
     response = redirect('/blogapp/')
     return response

    
