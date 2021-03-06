from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin, SearchFormViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin

from ...view_mixins import FormActionViewMixin, ModelsViewMixin


class BaseListboardView(EdcBaseViewMixin, FormActionViewMixin, SearchFormViewMixin,
                        ModelsViewMixin, NavbarViewMixin, ListboardFilterViewMixin,
                        ListboardView):

    navbar_name = 'specimens'
