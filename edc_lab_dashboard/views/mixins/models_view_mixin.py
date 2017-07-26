from django.apps import apps as django_apps


edc_lab_app_config = django_apps.get_app_config('edc_lab')


class ModelsViewMixin:

    @property
    def aliquot_model(self):
        return django_apps.get_model(*edc_lab_app_config.aliquot_model.split('.'))

    @property
    def box_model(self):
        return django_apps.get_model(*edc_lab_app_config.box_model.split('.'))

    @property
    def box_item_model(self):
        return django_apps.get_model(*edc_lab_app_config.box_item_model.split('.'))

    @property
    def manifest_model(self):
        return django_apps.get_model(*edc_lab_app_config.manifest_model.split('.'))

    @property
    def requisition_model(self):
        return django_apps.get_model(*edc_lab_app_config.requisition_model.split('.'))
