from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cms.ajax_views import (AjaxDetailView, AjaxCreateView , AjaxUpdateView, AjaxDeleteView)
from cms.mixins import ModelMixin
from .models import Todo
from .forms import TodoForm


class TodoList(ModelMixin, ListView):
    ajax_partial = 'todo/partials/todo_list_partial.html'
    model = Todo


class TodoDetail(AjaxDetailView, ModelMixin, DetailView):
    ajax_partial = 'todo/partials/todo_detail_partial.html'
    model = Todo


class TodoCreate(AjaxCreateView,ModelMixin, CreateView):
    model = Todo
    form_class = TodoForm
    ajax_partial = 'todo/partials/todo_form_partial.html'
    ajax_list_partial = 'todo/partials/todo_list_partial.html'


class TodoUpdate(AjaxUpdateView,ModelMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_form.html'
    ajax_partial = 'todo/partials/todo_form_partial.html'
    ajax_list_partial = 'todo/partials/todo_list_partial.html'


class TodoDelete(AjaxDeleteView, ModelMixin, DeleteView):
    model = Todo
    ajax_partial = 'todo/partials/todo_delete_partial.html'
    ajax_list_partial = 'todo/partials/todo_list_partial.html'
    success_url = reverse_lazy('todo:todo-list')
