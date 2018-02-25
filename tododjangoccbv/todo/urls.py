from django.urls import path

from .patterns import apps_dict, get_patterns
from .views import TodoListView

apps_dict['todo'] = {
    'app_name': 'todo',
    'filename': 'views'
}

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    # path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    #
    # path('create/', TodoCreateView.as_view(), name='todo-create'),
    # path('<int:pk>/update', TodoUpdateView.as_view(), name='todo-update'),
    # path('<int:pk>/delete', TodoDeleteView.as_view(), name='todo-delete'),
]

urlpatterns += get_patterns(apps_dict=apps_dict)

print(urlpatterns)
