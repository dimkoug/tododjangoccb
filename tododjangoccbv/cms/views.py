from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .mixins import BaseViewMixin, FormViewMixin


class CoreListView(BaseViewMixin, ListView):
    template = ''
    ajax_partial = ''
    model_name = ''
    app = ''
    def dispatch(self, *args, **kwargs):
        self.template = 'list'
        self.app = self.model._meta.app_label
        self.model_name = self.model.__name__.lower()
        self.ajax_partial = '{}/partials/{}_form_partial.html'.format(self.app,self.model_name)
        return super().dispatch(*args, **kwargs)

class CoreDetailView(BaseViewMixin, DetailView):
    template = ''
    model_name = ''
    app = ''
    def dispatch(self, *args, **kwargs):
        self.template = 'detail'
        self.app = self.model._meta.app_label
        self.model_name = self.model.__name__.lower()
        return super().dispatch(*args, **kwargs)


class CoreCreateView(FormViewMixin, CreateView):
    pass


class CoreUpdateView(FormViewMixin, UpdateView):
    pass


class CoreDeleteView(FormViewMixin, DeleteView):
    pass
