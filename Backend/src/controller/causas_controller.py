import json

from flask import request

from ..controller import controller
from ..service import CausasService
from ..repository import CausasRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'i_causas', methods=['GET'])
def causas(causas_service: CausasService, causas_repository: CausasRepository):
    # params causa
    causa = request.args.get('causa', default=0, type=int)
    return json.dumps(causas_service.get_causas(causas_repository, causa))
