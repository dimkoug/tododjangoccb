from django.urls import path

from cms.patterns import apps_dict, get_patterns
from .views import TodoListView

apps_dict['todo'] = {
    'app_name': 'todo',
    'filename': 'views'
}

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
]

urlpatterns += get_patterns(apps_dict=apps_dict)
