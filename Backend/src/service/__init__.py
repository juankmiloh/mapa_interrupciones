from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .anios_service import AniosService
from .causas_service import CausasService
from .empresas_service import EmpresasService
from .interrupciones_service import InterrupcionesService

class ServiceModule(Module):
    def configure(self, binder):
        anios_service = AniosService()
        causas_service = CausasService()
        empresas_service = EmpresasService()
        interrupciones_service = InterrupcionesService()

        binder.bind(AniosService, to=anios_service, scope=singleton)
        binder.bind(CausasService, to=causas_service, scope=singleton)
        binder.bind(EmpresasService, to=empresas_service, scope=singleton)
        binder.bind(InterrupcionesService, to=interrupciones_service, scope=singleton)
