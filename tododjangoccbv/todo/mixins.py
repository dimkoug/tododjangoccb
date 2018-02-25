from django.urls import reverse_lazy
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def checkPopup(obj, check):
    if check == 1:
        return HttpResponse(
            '''
            <script type="text/javascript">
                window.close();
                window.opener.location.reload();
            </script>
            '''
        )
    else:
        return HttpResponse(
        '''<script type="text/javascript">
        opener.dismissAddAnotherPopup(window, "{}", "{}");
        </script>'''.format(obj.pk, obj)
        )


class TabMixin:
    def form_valid(self, form):
        if self.request.GET.get('_popup'):
            form.save()
            tab = self.tab if hasattr(self, 'tab') else None
            if tab:
                return HttpResponse(
                    '''<script type="text/javascript">
                    opener.dismissPopupAndReload(window, "%s");
                    </script>''' % self.tab
                )
            else:
                obj = form.save()
                if 'is_list' in self.kwargs:
                    is_list = int(self.kwargs['is_list'])
                else:
                    is_list = int(self.request.GET.get('is_list'))
                check = is_list
                a = checkPopup(obj, check)
                return a
        else:
            return super(TabMixin, self).form_valid(form)


class BaseMixin:
    def get_data(self):
        url_name = self.url_name if hasattr(self, 'url_name') else 'list'
        return {
            'app_label': self.model._meta.app_label,
            'app_model': self.model.__name__.lower(),
            'url_name': url_name
        }


class ProtectedViewMixin:

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedViewMixin, self).dispatch(*args, **kwargs)


class SuccessUrl(BaseMixin):
    def get_success_url(self):
        data = self.get_data()
        return reverse_lazy('{}-{}-{}'.format(
            data['app_label'], data['app_model'], data['url_name']))


class AbsoluteUrlMixin(BaseMixin):
    '''
    Example:
        class Category(AbsoluteUrlMixin, models.Model):
            name = models.CharField(max_length=100)

            url_name = 'update'

        I use the convention as pattern:

            app_name-model_name-detail

    '''
    def get_absolute_url(self):
        kwargs = {}
        slug = hasattr(self, 'slug')
        url_name = hasattr(self, 'url_name')
        kwargs['pk'] = self.pk
        data = self.get_data()
        if not url_name:
            url_name = 'detail'
        if slug:
            kwargs['slug'] = self.slug
        return reverse_lazy('{}-{}-{}'.format(data['app_label'], data[
                            'app_model'], url_name), kwargs=kwargs)
