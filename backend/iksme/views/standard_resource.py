from backend.api import ModelResource, GET, LIST
from backend.extensions.api import api

from .blueprint import standard
from ..models import Standard


@api.model_resource(Standard, '/standards', '/standards/<slug>')
class StandardResource(ModelResource):
    include_methods = (GET, LIST)
    include_decorators = (GET,)

    # def get(self, article):
    #     prev, next = article.get_prev_next()
    #     return {'article': article,
    #             'prev': prev,
    #             'next': next}

    def list(self):
        return Standard.get_standards()
