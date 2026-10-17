from app import create_app, db
from app.models import Tren, TipoTren

app = create_app()

with app.app_context():
    locomotora = TipoTren(nombre="Locomotora")
    pasajeros = TipoTren(nombre="Pasajeros")
    db.session.add_all([
        locomotora, pasajeros,
        Tren(nombre="Tren de ejemplo 1", anio=1950, fabricante="Fabricante A",
             descripcion="Descripción de ejemplo.", tipo=locomotora),
        Tren(nombre="Tren de ejemplo 2", anio=1980, fabricante="Fabricante B",
             descripcion="Descripción de ejemplo.", tipo=pasajeros),
    ])
    db.session.commit()
    print("Datos cargados.")