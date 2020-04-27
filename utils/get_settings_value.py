from django.conf import settings

def get_setting_value(name):
    value = getattr(settings, name)
    if value is None:
        raise NotImplementedError("Parameter {} not configured%".format(name))
    return value