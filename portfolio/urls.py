from django.urls import path
from .views import HomeView


# adding url

urlpatterns = [
    path('', HomeView.as_view(), name='portfolio'),
]
