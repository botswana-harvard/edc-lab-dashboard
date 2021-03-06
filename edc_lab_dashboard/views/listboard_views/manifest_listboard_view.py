from django.apps import apps as django_apps
from edc_lab.constants import SHIPPED
from edc_lab.reports import ManifestReport
from edc_lab.models import Manifest

from ...model_wrappers import ManifestModelWrapper
from ..listboard_filters import ManifestListboardViewFilters
from .base_listboard_view import BaseListboardView

edc_lab_app_config = django_apps.get_app_config('edc_lab')


class ManifestListboardView(BaseListboardView):

    navbar_selected_item = 'manifest'

    form_action_url = 'manifest_form_action_url'
    listboard_url = 'manifest_listboard_url'
    listboard_template = 'manifest_listboard_template'
    model = edc_lab_app_config.manifest_model
    model_wrapper_cls = ManifestModelWrapper
    listboard_view_filters = ManifestListboardViewFilters()
    search_form_url = 'manifest_listboard_url'
    print_manifest_url = 'print_manifest_url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            new_manifest=ManifestModelWrapper(Manifest()),
            print_manifest_url_name=self.request.url_name_data[self.print_manifest_url],
            SHIPPED=SHIPPED)
        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get('pdf'):
            response = self.print_manifest()
            return response
        return super().get(request, *args, **kwargs)

    @property
    def manifest(self):
        return self.manifest_model.objects.get(
            manifest_identifier=self.request.GET.get('pdf'))

    def print_manifest(self):
        manifest_report = ManifestReport(
            manifest=self.manifest, user=self.request.user)
        return manifest_report.render()
