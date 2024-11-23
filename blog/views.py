from django.shortcuts import render, redirect
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})

def add_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        BlogPost.objects.create(title=title, content=content)
        return redirect('blog_list')
    return render(request, 'add_blog.html')

def delete_blog(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    post.delete()
    return redirect('blog_list')
