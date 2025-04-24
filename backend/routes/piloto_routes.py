from flask import Blueprint

pilotos = Blueprint('pilotos',__name__, url_prefix='/api/pilotos')

@pilotos.route('/')
def get_pilotos():
    return 'Get Pilotos'
