from django import template
from django.urls import reverse_lazy
register = template.Library()


@register.inclusion_tag('ajax/button_partial.html')
def show_modal_button(model):
    '''
    model is object

    '''
    app = model._meta.app_label
    model_name = model.__class__.__name__.lower()
    url_link = reverse_lazy('{}-{}-create'.format(app, model_name))
    return {'model_name': model_name, 'url': url_link}


@register.filter(name='url_list')
def url_list(model):
    '''
    model is object

    url convention:

    {{app_name}} - {{model}} - list

    '''
    app = model._meta.app_label
    model_name = model.__class__.__name__.lower()
    url_link = reverse_lazy('{}-{}-list'.format(app, model_name))
    return url_link


@register.filter(name='url_create')
def url_create(model):
    '''
    model is object

    url convention:

    {{app_name}} - {{model}} - create

    '''
    app = model._meta.app_label
    model_name = model.__class__.__name__.lower()
    url_link = reverse_lazy('{}-{}-create'.format(app, model_name))
    return url_link


@register.filter(name='url_detail')
def url_detail(model, pk):
    '''
    model is object

    url convention:

    {{app_name}} - {{model}} - detail

    '''
    app = model._meta.app_label
    model_name = model.__class__.__name__.lower()
    url_link = reverse_lazy(
        '{}-{}-detail'.format(app, model_name), kwargs={'pk': pk})
    return url_link


@register.filter(name='url_update')
def url_update(model, pk):
    '''
    model is object
    url convention:

    {{app_name}} - {{model}} - update
    '''
    app = model._meta.app_label
    model_name = model.__class__.__name__.lower()
    url_link = reverse_lazy(
        '{}-{}-update'.format(app, model_name), kwargs={'pk': pk})
    return url_link


@register.filter(name='url_delete')
def url_delete(model, pk):
    '''
    model is object

    url convention:

    {{app_name}} - {{model}} - delete

    '''
    app = model._meta.app_label
    model_name = model.__class__.__name__.lower()
    url_link = reverse_lazy(
        '{}-{}-delete'.format(app, model_name), kwargs={'pk': pk})
    return url_link


@register.filter(name='model_name')
def model_name(value):
    '''
    value is model object
    '''
    model = value.__class__.__name__.capitalize()
    return model


@register.filter(name='model_name_lower')
def model_name_lower(model):
    '''
    model is object

    '''
    app = model._meta.app_label
    model_name = model.__class__.__name__.lower()
    return model_name
