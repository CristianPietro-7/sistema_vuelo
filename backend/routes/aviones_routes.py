from flask import Blueprint

avion = Blueprint('avion',__name__,url_prefix='/api')

@avion.route('/aviones')
def get_aviones():
    return 'get aviones'
