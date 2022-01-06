from django.shortcuts import render

from blogproject.blog.models import Post

# Create your views here.


def post_pub_list(request):
  post = Post.objects.filter(status=1)
  data = {
    'pub_post': post,
  }
  return render(request, "post_list.html", data)

