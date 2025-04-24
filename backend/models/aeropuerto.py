from models.db import db

class Aeropuertos(db.Model):
    __tablaname__ = 'aeropuertos'

    idAeropuerto = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(25), unique=True, nullable=True)
    ciudad = db.Column(db.String(25))
    nombre = db.Column(db.String(25))
    pais = db.Column(db.String(25))


    def __init__(self, codigo, ciudad, nombre, pais):
        self.codigo = codigo
        self.ciudad = ciudad
        self.nombre = nombre
        self.pais = pais


    def serialize(self):
        return {
            'idAeropuerto': self.idAeropuerto,
            'codigo': self.codigo,
            'ciudad': self.ciudad,
            'nombre': self.nombre,
            'pais': self.pais

        }