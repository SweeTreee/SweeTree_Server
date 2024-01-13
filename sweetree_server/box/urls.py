from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views import (
    BoxViewSet
)


'''
    /box/                               # 생성      POST
    /box/<int:pk>                       # 단일 조회  GET
    /box/<int:pk>/                      # 수정      PATCH
'''


router = DefaultRouter()
router.register('box', BoxViewSet)

urlpatterns = [
    path('', include(router.urls))
]
