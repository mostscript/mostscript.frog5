import config
from patch import patch_access_logging
from patch import patch_tinymce_settings


def initialize(context):
    config.register()  # register plugin roles for collective.teamwork
    patch_access_logging()
    patch_tinymce_settings()

