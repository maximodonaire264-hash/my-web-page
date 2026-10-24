from . import db

class TipoTren(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    trenes = db.relationship("Tren", back_populates="tipo")
