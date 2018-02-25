from importlib import import_module
from django import forms

from .models import Todo


class DynamicForm:
    form_file_name = None

    def __init__(self, form_file_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self, 'form_file_name'):
            if self.form_file_name:
                self.form_file_name = self.form_file_name
            else:
                self.form_file_name = 'forms'
        app_module = import_module('{}.{}'.format(
            self.model._meta.app_label, self.form_file_name))
        form = getattr(app_module, '{}Form'.format(self.model.__name__))
        self.form_class = form


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('name',)
