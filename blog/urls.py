from .views import blog,PostDetail
from django.urls import path

urlpatterns = [
    path('home/', blog.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
