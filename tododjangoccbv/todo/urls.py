from django.urls import path

from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete


app_name = 'todo'
urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('create/', TodoCreate.as_view(), name='todo-create'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='todo-delete'),
]
