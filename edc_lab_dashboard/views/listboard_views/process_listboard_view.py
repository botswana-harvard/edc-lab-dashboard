from django.apps import apps as django_apps
from django.urls import reverse
from django.utils.safestring import mark_safe
from edc_constants.constants import YES

from ...dashboard_urls import dashboard_urls
from .requisition_listboard_view import RequisitionListboardView

app_config = django_apps.get_app_config('edc_lab_dashboard')


class ProcessListboardView(RequisitionListboardView):

    action_name = 'process'
    empty_queryset_message = 'All specimens have been process'
    form_action_url = 'process_form_action_url'
    listboard_template = 'process_listboard_template'
    listboard_url = 'process_listboard_url'
    navbar_selected_item = 'process'
    search_form_url = 'process_listboard_url'

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        options.update(
            is_drawn=YES,
            clinic_verified=YES,
            received=True,
            processed=False)
        return options

    @property
    def empty_queryset_message(self):
        href = reverse(dashboard_urls.get('pack_listboard_url'))
        return mark_safe(
            'All specimens have been processed. Continue to '
            f'<a href="{href}" class="alert-link">packing</a>')
