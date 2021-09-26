from django.urls import path
from .views import *

app_name = 'app'
urlpatterns = [
    path('', UserView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
]