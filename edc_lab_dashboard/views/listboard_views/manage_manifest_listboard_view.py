from django.apps import apps as django_apps
from edc_lab.constants import SHIPPED

from ...model_wrappers import ManifestItemModelWrapper
from ...view_mixins import ManifestViewMixin
from .base_listboard_view import BaseListboardView

edc_lab_app_config = django_apps.get_app_config('edc_lab')


class ManageManifestListboardView(ManifestViewMixin, BaseListboardView):

    action_name = 'manage'
    navbar_selected_item = 'manifest'
    form_action_url = 'manage_manifest_item_form_action_url'
    listboard_url = 'manage_manifest_listboard_url'
    listboard_template = 'manage_manifest_listboard_template'
    search_form_url = 'manage_manifest_listboard_url'

    model = edc_lab_app_config.manifest_item_model
    model_wrapper_cls = ManifestItemModelWrapper

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SHIPPED=SHIPPED,
            paginator_url_kwargs=self.url_kwargs,
        )
        return context

    @property
    def url_kwargs(self):
        return {
            'action_name': self.action_name,
            'manifest_identifier': self.manifest_identifier}
