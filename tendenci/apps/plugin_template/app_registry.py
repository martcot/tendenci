from tendenci.core.registry import site
from tendenci.core.registry.base import AppRegistry, lazy_reverse
from tendenci.apps.S_P_LOW.models import S_S_CAP


class S_S_CAPRegistry(AppRegistry):
    version = '1.0'
    author = 'Schipul - The Web Marketing Company'
    author_email = 'programmers@schipul.com'
    description = 'Create S_P_LOW type of content'

site.register(S_S_CAP, S_S_CAPRegistry)
