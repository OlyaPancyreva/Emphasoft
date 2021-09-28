from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()
router.register(r'api/v1/users', views.UserView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('djoser.urls.authtoken')),
    ]



