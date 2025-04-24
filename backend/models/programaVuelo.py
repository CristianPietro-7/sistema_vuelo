from models.db import db

class ProgramaVuelos(db.Model):
    __tablaname__ = 'programaVuelo'

    idPrograma = db.Column(db.Integer, primary_key=True)
    idAvion = db.Column(db.String(25))
    idVuelo = db.Column(db.String(25))
    ruta_vuelo = db.Column(db.String(25))
    escala_tecnica = db.Column(db.String(25))
    idAeropuerto_origen = db.Column(db.String(25))
    idAeropuerto_destino = db.Column(db.String(25))


    def __init__(self, idAvion, idVuelo,ruta_vuelo, escala_tecnica, idAeropuerto_origen, idAeropuerto_destino):
        self.idAvion = idAvion
        self.idVuelo = idVuelo
        self.ruta_vuelo = ruta_vuelo
        self.escala_tecnica = escala_tecnica
        self.idAeropuerto_origen = idAeropuerto_origen
        self.idAeropuerto_destino = idAeropuerto_destino


    def serialize(self):
        return {
            'idPrograma': self.idPrograma,
            'idAvion': self.idAvion,
            'idVuelo': self.idVuelo,
            'ruta_vuelo': self.ruta_vuelo,
            'escala_tecnica':self.escala_tecnica,
            'idAeropuerto_origen': self.idAeropuerto_origen,
            'idAeropuerto_destino': self.idAeropuerto_destino

        }