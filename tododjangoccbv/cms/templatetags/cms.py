from django import template
from django.urls import reverse_lazy
register = template.Library()


@register.simple_tag(takes_context=True)
def create_title(context, format_string):
    model = context['model']
    return '{} {}'.format(model.__name__.title(), format_string)


@register.simple_tag(takes_context=True)
def get_url(context, action, obj=None):
    model = context['model']
    app = model._meta.app_label
    lower_name = model.__name__.lower()
    if not obj:
        url_string = '{}:{}-{}'.format(app, lower_name, action)
        url = reverse_lazy(url_string)
    else:
        lower_name = obj.__class__.__name__.lower()
        url_string = '{}:{}-{}'.format(app, lower_name, action)
        if(hasattr(obj, 'uuid')):
            url = reverse_lazy(url_string, kwargs={'uuid': obj.uuid})
        elif(hasattr(obj, 'slug')):
            url = reverse_lazy(url_string, kwargs={'slug': obj.slug})
        else:
            url = reverse_lazy(url_string, kwargs={'pk': obj.pk})
    return url


@register.simple_tag(takes_context=True)
def get_model_name(context):
    model = context['model']
    return model.__name__.lower()


@register.simple_tag(takes_context=True)
def get_template_name(context, *args):
    model = context['model']
    app = model._meta.app_label
    lower_name = model.__name__.lower()
    template_name = "{}/partials/{}_list_partial.html".format(app,lower_name)
    return template_name
