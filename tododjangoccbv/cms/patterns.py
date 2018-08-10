from importlib import import_module
from django.urls import path
from django.apps import apps
apps_dict = {}


def get_patterns(apps_dict):
    '''
    apps_dict['app_name'] = {
        'app_name': 'app_name',
        'filename': 'views'
    }
    '''
    urlpatterns = []
    for key, value in apps_dict.items():
        app_module = import_module('{}.{}'.format(
            value['app_name'], value['filename']))
        app_models = apps.get_app_config(value['app_name']).get_models()
        for model in app_models:
            app_name = model._meta.app_label
            model_name = model.__name__
            model_name_lower = model.__name__.lower()
            listview = hasattr(app_module, '{}ListView'.format(model_name))
            if listview:
                listview = getattr(app_module, '{}ListView'.format(
                    model_name)).as_view()
                urlpatterns += [
                    path('{}/{}/'.format(app_name, model_name_lower),
                         listview,
                         name='{}-{}-list'.format(
                            app_name, model_name_lower))
                ]
            detailview = hasattr(app_module, '{}DetailView'.format(model_name))
            if detailview:
                detailview = getattr(app_module, '{}DetailView'.format(
                    model_name)).as_view()
                urlpatterns += [
                    path('{}/{}/<int:pk>/detail/'.format(
                         app_name, model_name_lower),
                         detailview,
                         name='{}-{}-detail'.format(
                            app_name, model_name_lower))
                ]
            addview = hasattr(app_module, '{}CreateView'.format(model_name))
            if addview:
                addview = getattr(app_module, '{}CreateView'.format(
                    model_name)).as_view()
                urlpatterns += [
                    path('{}/{}/add/'.format(app_name, model_name_lower),
                         addview,
                         name='{}-{}-create'.format(
                            app_name, model_name_lower))
                ]
            updateview = hasattr(app_module, '{}UpdateView'.format(
                model_name))
            if updateview:
                updateview = getattr(app_module, '{}UpdateView'.format(
                    model_name)).as_view()
                urlpatterns += [
                    path('{}/{}/<int:pk>/'.format(
                         app_name, model_name_lower),
                         updateview,
                         name='{}-{}-update'.format(
                            app_name, model_name_lower))
                ]
            deleteview = hasattr(app_module, '{}DeleteView'.format(
                model_name))
            if deleteview:
                deleteview = getattr(app_module, '{}DeleteView'.format(
                    model_name)).as_view()
                urlpatterns += [
                    path('{}/{}/<int:pk>/delete/'.format(
                        app_name, model_name_lower),
                        deleteview,
                        name='{}-{}-delete'.format(
                            app_name, model_name_lower))
                ]
    return urlpatterns
