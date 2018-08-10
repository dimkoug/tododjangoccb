from cms.views import (CmsListView, CmsDetailView, CmsCreateView,
                       CmsUpdateView, CmsDeleteView)
from cms.ajax_views import (AjaxCreateView, AjaxUpdateView, AjaxDeleteView)
from .models import Todo
from .forms import TodoForm


class TodoListView(CmsListView):
    template_name_suffix = '/list'
    model = Todo


class TodoDetailView(CmsDetailView):
    template_name_suffix = '/detail'
    model = Todo


class TodoCreateView(AjaxCreateView, CmsCreateView):
    ajax_list = 'todo/todo/partial_list.html'
    model = Todo
    form_class = TodoForm


class TodoUpdateView(AjaxUpdateView, CmsUpdateView):
    ajax_list = 'todo/todo/partial_list.html'
    model = Todo
    form_class = TodoForm


class TodoDeleteView(AjaxDeleteView, CmsDeleteView):
    ajax_list = 'todo/todo/partial_list.html'
    model = Todo
