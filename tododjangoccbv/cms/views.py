from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .mixins import BaseViewMixin, FormViewMixin


class CoreListView(BaseViewMixin, ListView):
    pass

class CoreDetailView(BaseViewMixin, DetailView):
    pass


class CoreCreateView(FormViewMixin, CreateView):
    pass


class CoreUpdateView(FormViewMixin, UpdateView):
    pass


class CoreDeleteView(FormViewMixin, DeleteView):
    pass
