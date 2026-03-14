from database import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    tipo_usuario = db.Column(db.String(20), nullable=False)  # candidato ou empresa
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    salario = db.Column(db.Float)
    localizacao = db.Column(db.String(100))
    empresa_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)