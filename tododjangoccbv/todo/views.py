from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cms.ajax_views import (AjaxDetailView, AjaxCreateView , AjaxUpdateView, AjaxDeleteView)
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


class TodoUpdate(AjaxUpdateView):
    model = Todo
    form_class = TodoForm


class TodoDelete(AjaxDeleteView):
    model = Todo
