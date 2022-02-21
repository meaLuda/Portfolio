from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# model from blog app
from blog.models import Post
from django.views import generic
# Create your views here.

class HomeView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:2]
    template_name = 'portfolio/home.html'
