from django.shortcuts import render

from blogproject.blog.models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    c = {'post_list': posts,}
    return render(request,'post_list.html', c)