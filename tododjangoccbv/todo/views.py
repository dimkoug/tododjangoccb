from cms.views import (CmsListView, CmsDetailView, CmsCreateView,
                       CmsUpdateView, CmsDeleteView)
from cms.ajax_views import (AjaxCreateUpdateView, AjaxDeleteView)
from .models import Todo
from .forms import TodoForm


class TodoListView(CmsListView):
    template_name_suffix = '/list'
    model = Todo


class TodoDetailView(CmsDetailView):
    template_name_suffix = '/detail'
    model = Todo


class TodoCreateView(AjaxCreateUpdateView, CmsCreateView):
    model = Todo
    form_class = TodoForm


class TodoUpdateView(AjaxCreateUpdateView, CmsUpdateView):
    model = Todo
    form_class = TodoForm


class TodoDeleteView(AjaxDeleteView, CmsDeleteView):
    model = Todo
