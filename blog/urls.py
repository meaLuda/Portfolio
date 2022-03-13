from .views import blog,PostDetail
from django.urls import path

urlpatterns = [
    path('', blog.as_view(),name='blog'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
