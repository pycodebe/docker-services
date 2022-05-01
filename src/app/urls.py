from django.urls import include, path
from .views import TaskView

urlpatterns = [
    path('run_a_task', TaskView.as_view(), name="make a task"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]