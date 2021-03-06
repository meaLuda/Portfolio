from django.shortcuts import redirect, render

# Create your views here.

from django.views import generic
from .models import Post
from django.shortcuts import redirect

class blog(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
