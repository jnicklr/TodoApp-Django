from appTodo.api.serializers import TaskSerializer
from appTodo.models import Task
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = LimitOffsetPagination
    