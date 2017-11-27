from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from edc_constants.constants import YES

from ...model_wrappers import RequisitionModelWrapper
from ...view_mixins import StudySiteNameQuerysetViewMixin
from ..listboard_filters import RequisitionListboardViewFilters
from .base_listboard_view import BaseListboardView

edc_lab_app_config = django_apps.get_app_config('edc_lab')


class RequisitionListboardView(StudySiteNameQuerysetViewMixin, BaseListboardView):

    form_action_url = 'requisition_action_url'
    listboard_template = 'requisition_listboard_template'
    listboard_url = 'requisition_listboard_url'
    listboard_view_filters = RequisitionListboardViewFilters()
    model = edc_lab_app_config.requisition_model
    model_wrapper_cls = RequisitionModelWrapper
    navbar_selected_item = 'requisition'
    show_all = True
    search_form_url = 'requisition_listboard_url'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        options.update(is_drawn=YES)
        return options
