from django.conf.urls import url, include
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/users', views.UserView)

urlpatterns = [
    url(r'^', include(router.urls)),
    ]



