from flask import Blueprint
from flask_cors import CORS

controller = Blueprint('controller', __name__, url_prefix='/')
# src.controller

from . import \
front_controller, \
anios_controller, \
causas_controller, \
empresas_controller, \
interrupciones_controller
