from django.apps import apps as django_apps
from django.urls import reverse
from django.utils.safestring import mark_safe
from edc_constants.constants import YES

from .requisition_listboard_view import RequisitionListboardView

app_config = django_apps.get_app_config('edc_lab_dashboard')


class ReceiveListboardView(RequisitionListboardView):

    action_name = 'receive'
    form_action_url = 'receive_form_action_url'
    listboard_template = 'receive_listboard_template'
    listboard_url = 'receive_listboard_url'
    navbar_selected_item = 'receive'
    process_listboard_url = 'process_listboard_url'
    show_all = True
    search_form_url = 'receive_listboard_url'

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        options.update(
            is_drawn=YES,
            clinic_verified=YES,
            received=False, processed=False)
        return options

    @property
    def empty_queryset_message(self):
        href = reverse(self.request.url_name_data['process_listboard_url'])
        return mark_safe(
            'All specimens have been received. Continue to '
            f'<a href="{href}" class="alert-link">processing</a>')
