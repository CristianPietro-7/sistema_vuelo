from flask import Flask
from flask_cors import CORS
from models.db import db
from config.config import DATABASE_CONNECTION_URI
from routes.piloto_routes import pilotos
from routes.aeropuerto_routes import aeropuerto
from routes.aviones_routes import avion

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(pilotos)
app.register_blueprint(aeropuerto)
app.register_blueprint(avion)

with app.app_context():
    from models.aeropuerto import Aeropuertos
    from models.avion import Aviones
    from models.piloto import Pilotos
    from models.programaVuelo import ProgramaVuelos
    from models.vuelo import Vuelos
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
