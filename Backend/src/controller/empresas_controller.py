import json

from flask import request

from ..controller import controller
from ..service import EmpresasService
from ..repository import EmpresasRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'i_empresas', methods=['GET'])
def empresas(empresas_service: EmpresasService, empresas_repository: EmpresasRepository):
    # params empresa
    empresa = request.args.get('empresa', default=0, type=int)
    return json.dumps(empresas_service.get_empresas(empresas_repository, empresa))
