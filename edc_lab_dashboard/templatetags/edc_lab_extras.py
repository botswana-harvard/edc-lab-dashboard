from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils.safestring import mark_safe

from edc_lab.constants import SHIPPED
from edc_lab.models import BoxItem
from django.templatetags.i18n import BlockTranslateNode

register = template.Library()


@register.inclusion_tag('edc_lab_dashboard/listboard/box/box_cell.html')
def show_box_rows(box, listboard_url, position=None):
    """Returns rendered HTML of a box as a dictionary of keys headers, rows.

    Usage::

        {% block results_body %}
            {% show_box_rows box listboard_url position=position %}
        {% endblock results_body %}

    """
    position = '0' if position is None else str(position)
    btn_style = {
        -1: 'btn-danger',
        0: 'btn-default',
        1: 'btn-success'}
    pos = 0
    rows = []
    header = range(1, box.box_type.across + 1)
    for i in range(1, box.box_type.down + 1):
        row = {}
        reverse_kwargs = {}
        row['position'] = i
        row['cells'] = []
        for _ in range(1, box.box_type.across + 1):
            cell = {}
            pos += 1
            try:
                box_item = box.boxitem_set.get(position=pos)
            except ObjectDoesNotExist:
                box_item = BoxItem(box=box)
            reverse_kwargs = {
                'position': pos,
                'box_identifier': box.box_identifier,
                'action_name': 'verify'}
            cell['href'] = reverse(listboard_ur, kwargs=reverse_kwargs)
            cell['btn_style'] = btn_style.get(box_item.verified)
            cell['btn_label'] = str(pos).zfill(2)
            cell['btn_title'] = box_item.human_readable_identifier or 'empty'
            cell['has_focus'] = str(pos) == position
            cell['box_item'] = box_item
            row['cells'].append(cell)
        rows.append(row)
    return {'headers': header, 'rows': rows}


@register.filter(is_safe=True)
def verified(box_item):
    """Returns a safe HTML check mark string if a Box item has been verified.
    """
    if not box_item.verified:
        verified = False
    elif box_item.verified == 1:
        verified = True
    elif box_item.verified == -1:
        verified = False
    return '' if not verified else mark_safe(
        '&nbsp;<span title="verified" alt="verified" class="text text-success">'
        '<i class="fa fa-check fa-fw"></i></span>')


@register.filter(is_safe=True)
def shipped(box_item):
    """Returns a safe HTML check mark string if a Box item has been shipped.
    """
    return '' if not box_item.status == SHIPPED else mark_safe(
        '&nbsp;<span title="shipped" class="text text-success">'
        '<i class="fa fa-ship fa-fw"></i></span>')
