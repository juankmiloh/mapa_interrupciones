from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .anios_repository import AniosRepository
from .causas_repository import CausasRepository
from .empresas_repository import EmpresasRepository
from .interrupciones_repository import InterrupcionesRepository


class RepositoryModule(Module):
    def __init__(self, db):
        self.db = db

    def configure(self, binder):
        anios_repository = AniosRepository(self.db)
        causas_repository = CausasRepository(self.db)
        empresas_repository = EmpresasRepository(self.db)
        interrupciones_repository = InterrupcionesRepository(self.db)

        binder.bind(AniosRepository, to=anios_repository, scope=singleton)
        binder.bind(CausasRepository, to=causas_repository, scope=singleton)
        binder.bind(EmpresasRepository, to=empresas_repository, scope=singleton)
        binder.bind(InterrupcionesRepository, to=interrupciones_repository, scope=singleton)
