from django.http import JsonResponse
from django.template.loader import render_to_string


class AjaxListView:
    ajax_list = 'cms/ajax/partial_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        context['model'] = self.model
        context['name'] = '{} List'.format(self.model.__name__)
        return context


class AjaxCreateView:
    ajax_partial = 'cms/ajax/create_partial.html'
    ajax_list = 'cms/ajax/partial_list.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        context = self.get_context_data()
        if request.is_ajax():
            html_form = render_to_string(self.ajax_partial, context, request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        data = dict()
        context = self.get_context_data()
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['list'] = render_to_string(
                self.ajax_list, context, self.request)
        else:
            data['form_is_valid'] = False
        data['html_form'] = render_to_string(
            self.ajax_partial, context, request=self.request)

        if self.request.is_ajax():
            return JsonResponse(data)
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        data = dict()
        context = self.get_context_data()
        data['form_is_valid'] = False
        data['html_form'] = render_to_string(
            self.ajax_partial, context, request=self.request)

        if self.request.is_ajax():
            return JsonResponse(data)
        else:
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        context['model'] = self.model
        context['name'] = '{} Create'.format(self.model.__name__)
        return context


class AjaxUpdateView:
    ajax_partial = 'cms/ajax/update_partial.html'
    ajax_list = 'cms/ajax/partial_list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if request.is_ajax():
            html_form = render_to_string(self.ajax_partial, context, request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        data = dict()
        context = self.get_context_data()
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['list'] = render_to_string(
                self.ajax_list, context, self.request)
        else:
            data['form_is_valid'] = False
        data['html_form'] = render_to_string(
            self.ajax_partial, context, request=self.request)

        if self.request.is_ajax():
            return JsonResponse(data)
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        data = dict()
        context = self.get_context_data()
        data['form_is_valid'] = False
        data['html_form'] = render_to_string(
            self.ajax_partial, context, request=self.request)

        if self.request.is_ajax():
            return JsonResponse(data)
        else:
            return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        context['model'] = self.model
        context['name'] = '{} Update'.format(self.model.__name__)
        return context


class AjaxDeleteView:
    ajax_partial = 'cms/ajax/delete_partial.html'
    ajax_list = 'cms/ajax/partial_list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if request.is_ajax():
            html_form = render_to_string(self.ajax_partial, context, request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        if self.request.is_ajax():
            self.object = self.get_object()
            self.object.delete()
            data = dict()
            data['form_is_valid'] = True
            context = self.get_context_data()
            context['object_list'] = self.model.objects.all()
            data['list'] = render_to_string(
                self.ajax_list, context, self.request)
            return JsonResponse(data)
        else:
            return self.delete(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        context['name'] = '{} Delete'.format(self.model.__name__)
        return context
