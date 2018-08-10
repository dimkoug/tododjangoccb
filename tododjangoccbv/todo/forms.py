from django import forms

from cms.forms import BootstrapHelperForm

from .models import Todo


class TodoForm(BootstrapHelperForm, forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('name',)
