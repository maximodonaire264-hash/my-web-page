from . import db

class TipoTren(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    trenes = db.relationship("Tren", back_populates="tipo")

class Tren(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    anio = db.Column(db.Integer)
    fabricante = db.Column(db.String(120))
    descripcion = db.Column(db.Text)
    imagen = db.Column(db.String(200))
    tipo_id = db.Column(db.ForeignKey("tipo_tren.id"))
    tipo = db.relationship("TipoTren", back_populates="trenes")