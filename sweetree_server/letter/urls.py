from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from box.views import BoxViewSet
from letter.views import LetterViewSet


'''
    /box/<int:pk>/letters/                              # 생성      POST
    /box/<int:pk>/letters/check/                        # 단일 조회  GET
    /box/<int:pk>/letters/count/                        # 수정      PATCH
'''

router = DefaultRouter()
router.register(r'box', BoxViewSet)

box_router = routers.NestedSimpleRouter(router, r'box', lookup='box')
box_router.register(r'letters', LetterViewSet, basename='box-letters')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(box_router.urls)),
]
