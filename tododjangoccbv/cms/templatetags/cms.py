from django import template
from django.urls import reverse_lazy
register = template.Library()


@register.simple_tag(takes_context=True)
def create_title(context, format_string):
    model = context['model']
    return '{} {}'.format(model.__name__.title(), format_string)


@register.simple_tag(takes_context=True)
def create_url(context, format_string):
    model = context['model']
    app = model._meta.app_label
    model_name = model.__name__.lower()
    return reverse_lazy('{}-{}-{}'.format(app, model_name, format_string))


@register.simple_tag
def create_object_url(object, format_string):
    app = object._meta.app_label
    model_name = object.__class__.__name__.lower()
    url_link = reverse_lazy(
        '{}-{}-{}'.format(app, model_name, format_string),
        kwargs={'pk': object.pk})
    return url_link


@register.simple_tag(takes_context=True)
def get_model_name(context):
    model = context['model']
    return model.__name__.lower()
