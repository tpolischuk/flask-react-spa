from backend.api import ModelResource, GET, LIST
from backend.extensions.api import api

from .blueprint import iksme
from ..models import Standard

@api.model_resource(Standard, '/standards', '/standards/<slug>')
class StandardResource(ModelResource):
    include_methods = (GET, LIST)
    include_decorators = (GET,)

    def get(self):
        print('WHERE AM I')
        return 'blah blah blah blah'

    def list(self):
        print('WHERE AM I in list')
        return 'blah blah blah blah'

    # def get(self, article):
    #     prev, next = article.get_prev_next()
    #     return {'article': article,
    #             'prev': prev,
    #             'next': next}

    # def get(self):
    #     return Standard.get_standards()
