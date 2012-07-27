from tendenci.core.registry import site
from tendenci.core.registry.base import AppRegistry, lazy_reverse
from tendenci.apps.quotes.models import Quote


class QuoteRegistry(AppRegistry):
    version = '1.0'
    author = 'Schipul - The Web Marketing Company'
    author_email = 'programmers@schipul.com'
    description = 'Create quotes that can be rotated or listed on the site'
    
    event_logs = {
        'quote':{
            'base':('150000','FFEE44'),
            'add':('150100','119933'),
            'edit':('150200','EEDD55'),
            'delete':('150300','AA2222'),
            'search':('154000','CC55EE'),
            'view':('155000','55AACC'),
        }
    }

site.register(Quote, QuoteRegistry)
