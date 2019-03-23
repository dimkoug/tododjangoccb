from django.http import JsonResponse
from django import template
from django.template.loader import render_to_string


class AjaxCreateUpdateView:
    def get(self, request, *args, **kwargs):
        if 'pk' not in self.kwargs:
            self.object = None
        else:
            self.object = self.get_object()
        context = self.get_context_data()
        self.ajax_partial = 'ajax/{}_form_partial.html'.format(
            self.model.__name__.lower())
        self.ajax_list = 'ajax/{}_list_partial.html'.format(
            self.model.__name__.lower())
        if request.is_ajax():
            try:
                html_form = render_to_string(
                    self.ajax_partial, context, request)
            except template.TemplateDoesNotExist:
                html_form = render_to_string(
                    'cms/ajax/create_update_form_partial.html', context,
                    request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        return context

    def form_valid(self, form):
        self.ajax_partial = 'ajax/{}_form_partial.html'.format(
            self.model.__name__.lower())
        self.ajax_list = 'ajax/{}_list_partial.html'.format(
            self.model.__name__.lower())
        data = dict()
        context = self.get_context_data()
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            try:
                data['list'] = render_to_string(
                    self.ajax_list, context, self.request)
            except template.TemplateDoesNotExist:
                data['list'] = render_to_string(
                    'cms/ajax/list_partial.html', context, self.request)
        else:
            data['form_is_valid'] = False
        try:
            data['html_form'] = render_to_string(
                self.ajax_partial, context, request=self.request)
        except template.TemplateDoesNotExist:
            data['html_form'] = render_to_string(
                'cms/ajax/create_update_form_partial',
                context, request=self.request)

        if self.request.is_ajax():
            return JsonResponse(data)
        else:
            return super().form_valid(form)


class AjaxDeleteView:
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        self.ajax_partial = 'ajax/delete_partial.html'
        self.ajax_list = 'ajax/{}_list_partial.html'.format(
            self.model.__name__.lower())
        if request.is_ajax():
            try:
                html_form = render_to_string(
                    self.ajax_partial, context, request)
            except template.TemplateDoesNotExist:
                html_form = render_to_string(
                    'cms/ajax/delete_partial.html', context, request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        self.ajax_partial = 'ajax/delete_partial.html'
        self.ajax_list = 'ajax/{}_list_partial.html'.format(
            self.model.__name__.lower())
        if self.request.is_ajax():
            self.object = self.get_object()
            self.object.delete()
            data = dict()
            data['form_is_valid'] = True
            context = self.get_context_data()
            context['object_list'] = self.model.objects.all()
            try:
                data['list'] = render_to_string(
                    self.ajax_list, context, self.request)
            except template.TemplateDoesNotExist:
                data['list'] = render_to_string(
                    'cms/ajax/list_partial.html', context, self.request)
            return JsonResponse(data)
        else:
            return self.delete(*args, **kwargs)
