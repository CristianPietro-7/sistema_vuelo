from models.db import db

class Vuelos(db.Model):
    __tablaname__ = 'vuelos'

    idVuelos = db.Column(db.Integer, primary_key=True)
    nro_vuelo = db.Column(db.String(25), unique=True, nullable=True)
    linea_aerea = db.Column(db.String(25))
    fecha = db.Column(db.String(25))
    plazas_vacantes = db.Column(db.String(25))


    def __init__(self, nro_vuelo, linea_aerea, fecha, plazas_vacantes):
        self.nro_vuelo = nro_vuelo
        self.linea_aerea = linea_aerea
        self.fecha = fecha
        self.plazas_vacantes = plazas_vacantes


    def serialize(self):
        return {
            'idVuelos': self.idVuelos,
            'nro_vuelo': self.nro_vuelo,
            'linea_aerea': self.linea_aerea,
            'fecha': self.fecha,
            'plazas_vacantes': self.plazas_vacantes

        }