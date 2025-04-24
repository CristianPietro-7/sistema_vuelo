from flask import Blueprint

aeropuerto = Blueprint('aeropuerto',__name__,url_prefix='/api')

@aeropuerto.route('/aeropuerto')
def get_aeropuertos():
    return 'Get aeropouertos'