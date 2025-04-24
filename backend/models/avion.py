from models.db import db

class Aviones(db.Model):
    __tablaname__ = 'aviones'

    idAviones = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(25), unique=True, nullable=True)
    capacidad = db.Column(db.String(25))
    envergadura = db.Column(db.String(25))
    velocidad_crucero = db.Column(db.String(25))


    def __init__(self, codigo, capacidad, envergadura, velocidad_crucero):
        self.codigo = codigo
        self.capacidad = capacidad
        self.envergadura = envergadura
        self.velocidad_crucero = velocidad_crucero


    def serialize(self):
        return {
            'idAviones': self.idAviones,
            'codigo': self.codigo,
            'capacidad': self.capacidad,
            'envergadura': self.envergadura,
            'velocidad_crucero': self.velocidad_crucero

        }