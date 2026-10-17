from flask import Blueprint, render_template, request
from .models import Tren, TipoTren

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    destacados = Tren.query.limit(3).all()
    return render_template("index.html", destacados=destacados)

@bp.route("/catalogo")
def catalogo():
    return render_template("catalogo.html",
                           trenes=Tren.query.all(),
                           tipos=TipoTren.query.all())

@bp.route("/catalogo/buscar")
def buscar():
    q = request.args.get("q", "").strip()
    tipo = request.args.get("tipo", "")
    consulta = Tren.query
    if q:
        consulta = consulta.filter(Tren.nombre.ilike(f"%{q}%"))
    if tipo.isdigit():
        consulta = consulta.filter(Tren.tipo_id == int(tipo))
    return render_template("_lista_trenes.html", trenes=consulta.all())

@bp.route("/tren/<int:tren_id>")
def tren_detalle(tren_id):
    tren = Tren.query.get_or_404(tren_id)
    return render_template("tren_detalle.html", tren=tren)