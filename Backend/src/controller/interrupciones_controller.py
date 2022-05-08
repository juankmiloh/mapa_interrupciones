import json

from flask import request

from . import controller
from ..service import InterrupcionesService
from ..repository import InterrupcionesRepository
from ..util.constants import API_ROOT_PATH

# Obtener listado de interrupciones
@controller.route(API_ROOT_PATH + 'i_interrupcion', methods=['GET'])
def interrupciones(interrupciones_service: InterrupcionesService, interrupciones_repository: InterrupcionesRepository):
    return interrupciones_service.get_interrupciones(interrupciones_repository, anio=0, mes=0, empresa=0, causa=0)

# Obtener listado de interrupciones X anio
@controller.route(API_ROOT_PATH + 'i_interrupcion/<int:anio>', methods=['GET'])
def interrupciones_v1(interrupciones_service: InterrupcionesService, interrupciones_repository: InterrupcionesRepository, anio):
    return interrupciones_service.get_interrupciones(interrupciones_repository, anio=anio, mes=0, empresa=0, causa=0)

# Obtener listado de interrupciones X anio X mes
@controller.route(API_ROOT_PATH + 'i_interrupcion/<int:anio>/<int:mes>', methods=['GET'])
def interrupciones_v2(interrupciones_service: InterrupcionesService, interrupciones_repository: InterrupcionesRepository, anio, mes):
    return interrupciones_service.get_interrupciones(interrupciones_repository, anio=anio, mes=mes, empresa=0, causa=0)

# Obtener listado de interrupciones X anio X mes X empresa
@controller.route(API_ROOT_PATH + 'i_interrupcion/<int:anio>/<int:mes>/<int:empresa>', methods=['GET'])
def interrupciones_v3(interrupciones_service: InterrupcionesService, interrupciones_repository: InterrupcionesRepository, anio, mes, empresa):
    return interrupciones_service.get_interrupciones(interrupciones_repository, anio=anio, mes=mes, empresa=empresa, causa=0)

# Obtener listado de interrupciones X anio X mes X empresa X causa
@controller.route(API_ROOT_PATH + 'i_interrupcion/<int:anio>/<int:mes>/<int:empresa>/<int:causa>', methods=['GET'])
def interrupciones_v4(interrupciones_service: InterrupcionesService, interrupciones_repository: InterrupcionesRepository, anio, mes, empresa, causa):
    return interrupciones_service.get_interrupciones(interrupciones_repository, anio=anio, mes=mes, empresa=empresa, causa=causa)
