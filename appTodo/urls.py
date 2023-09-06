from django.urls import path, include
from rest_framework import routers
from appTodo.api.viewsets import TaskViewSet
from .views import home

router = routers.DefaultRouter()
router.register('', TaskViewSet, basename='api')

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', home, name='home')
]
