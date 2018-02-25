from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .mixins import SuccessUrl
from .forms import DynamicForm


class CmsView(TemplateView):
    template_name = "cms/index.html"


class CmsListView(ListView):
    template_name_suffix = '/list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        context['name'] = '{} List'.format(self.model.__name__)
        return context


class CmsDetailView(DetailView):
    template_name_suffix = '/detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        context['list'] = '{} '.format(self.model.__name__.capitalize())
        context['name'] = '{} Detail'.format(self.get_object())
        return context


class CmsCreateView(DynamicForm, SuccessUrl, CreateView):
    template_name_suffix = '/form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        context['list'] = '{} '.format(self.model.__name__.capitalize())
        context['name'] = '{} Create'.format(self.model.__name__)
        return context


class CmsUpdateView(DynamicForm, SuccessUrl, UpdateView):
    template_name_suffix = '/form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        context['list'] = '{} '.format(self.model.__name__.capitalize())
        context['name'] = '{} Update'.format(self.get_object())
        return context


class CmsDeleteView(SuccessUrl, DeleteView):
    template_name_suffix = '/delete'
