from django.http import JsonResponse
from django import template
from django.template.loader import render_to_string


class CreateUpdateForm:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.get_queryset()
        return context

    def form_valid(self, form):
        data = dict()
        context = self.get_context_data()
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['list'] = render_to_string(
                self.ajax_list_partial, context, self.request)
        else:
            data['form_is_valid'] = False
        data['html_form'] = render_to_string(
            self.ajax_partial, context, request=self.request)

        if self.request.is_ajax():
            return JsonResponse(data)
        else:
            return super().form_valid(form)


class AjaxListView:
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        if request.is_ajax():
            html_form = render_to_string(
                self.ajax_partial, context, request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

class AjaxDetailView:
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if request.is_ajax():
            html_form = render_to_string(
                self.ajax_partial, context, request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

class AjaxCreateView(CreateUpdateForm):
    def get(self, request, *args, **kwargs):
        self.object = None
        context = self.get_context_data()

        if request.is_ajax():
            html_form = render_to_string(
                self.ajax_partial, context, request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

class AjaxUpdateView(CreateUpdateForm):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if request.is_ajax():
            html_form = render_to_string(
                self.ajax_partial, context, request)
            return JsonResponse({'html_form': html_form})
        else:
            return super().get(request, *args, **kwargs)

class AjaxDeleteView:
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if request.is_ajax():
            html_form = render_to_string(
                self.ajax_partial, context, request)

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
            context['object_list'] = self.get_queryset()
            data['list'] = render_to_string(
                self.ajax_list_partial, context, self.request)
            return JsonResponse(data)
        else:
            return self.delete(*args, **kwargs)
