from cms.ajax_views import (
    AjaxDetailView, AjaxCreateView, AjaxUpdateView, AjaxDeleteView
)
from cms.mixins import ModelMixin
from cms.views import CoreListView
from .models import Todo
from .forms import TodoForm


class TodoList(CoreListView):
    model = Todo


class TodoDetail(AjaxDetailView):
    model = Todo


class TodoCreate(AjaxCreateView):
    model = Todo
    form_class = TodoForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TodoUpdate(AjaxUpdateView):
    model = Todo
    form_class = TodoForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TodoDelete(AjaxDeleteView):
    model = Todo
