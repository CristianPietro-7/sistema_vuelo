from models.db import db


class Pilotos(db.Model):
    __tablename__ = 'pilotos'

    idPilotos = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(25), unique=True, nullable=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    telefono = db.Column(db.String(25))
    email = db.Column(db.String(150), unique=True, nullable=True)
    licencia = db.Column(db.String(150))
    fecha_nac = db.Column(db.Date) 


    def __init__(self, dni, nombre, apellido, telefono, email, licencia, fecha_nac):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.licencia = licencia
        self.fecha_nac = fecha_nac

    def serialize(self):
        return {
            'idPilotos': self.idPilotos,
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'email': self.email,
            'licencia': self.licencia,
            'fecha_nac': self.fecha_nac.strftime('%Y-%m-%d') if self.fecha_nac else None
        }