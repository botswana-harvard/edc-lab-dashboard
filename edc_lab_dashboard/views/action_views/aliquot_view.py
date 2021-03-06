from django.contrib import messages
from edc_base.view_mixins import EdcBaseViewMixin
from edc_lab import AliquotLabel, LabPrintersMixin
from edc_label import add_job_results_to_messages

from ...view_mixins import ModelsViewMixin
from .action_view import ActionView


class AliquotView(EdcBaseViewMixin, ModelsViewMixin, LabPrintersMixin, ActionView):

    post_action_url = 'aliquot_listboard_url'
    valid_form_actions = ['print_labels']
    action_name = 'aliquot'
    label_cls = AliquotLabel

    def process_form_action(self, request=None):
        if self.action == 'print_labels':
            if not self.selected_items:
                message = ('Nothing to do. No items have been selected.')
                messages.warning(request, message)
            else:
                job_result = self.print_labels(
                    pks=self.selected_items, request=request)
                if job_result:
                    add_job_results_to_messages(request, [job_result])
                else:
                    messages.error(
                        request,
                        f'Failed to print. Selected items were {self.selected_items}.')
