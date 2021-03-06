from django.apps import apps as django_apps

from ...view_mixins import BoxViewMixin
from .base_listboard_view import BaseListboardView

edc_lab_app_config = django_apps.get_app_config('edc_lab')


class BaseBoxItemListboardView(BoxViewMixin, BaseListboardView):

    navbar_selected_item = 'pack'
    ordering = ('-position', )
    model = edc_lab_app_config.box_item_model

    def get_queryset_filter_options(self, request, *args, **kwargs):
        return {'box': self.box}
