from flask import Blueprint

vuelos = Blueprint('vuelos',__name__,url_prefix='/api')

@vuelos.route('/vuelos')
def get_vuelos():
    return 'Get vuelos'