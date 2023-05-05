from django.urls import path, include
from rest_framework import routers

from app import views
from app.views import UserViewSet, PostDetail, PostCreate, Test

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('', include(router.urls)),
    path('post/<int:id>', PostDetail.as_view(), name="post-detail"),
    path('post/', PostCreate.as_view(), name="post-create"),
    path('test/', Test.as_view(), name="test"),
]
