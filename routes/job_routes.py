from flask import Blueprint, request, jsonify
from models import Job
from models import User
from models import Application
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from flask_jwt_extended import jwt_required, get_jwt_identity

job_auth = Blueprint("jobs", __name__)

@job_auth.route("/job", methods=["POST"])
@jwt_required()
def create_job():
    user_id = int(get_jwt_identity())

    user = User.query.get(user_id)

    if user.tipo_usuario != 'empresa':
        return jsonify({"error": "Apenas empresas podem criar vagas"}), 403

    data = request.json

    titulo = data.get("titulo")
    descricao = data.get("descricao")
    salario = data.get("salario")
    
    job = Job(
        titulo = titulo,
        descricao = descricao,
        salario = salario,
        empresa_id = user.id
    )

    db.session.add(job)
    db.session.commit()

    return jsonify({"message": "Vaga criada com sucesso"}), 201


@job_auth.route("/jobs/<int:job_id>/apply", methods=["POST"])
@jwt_required()
def apply_job(job_id):

    user_id = int(get_jwt_identity())

    user = User.query.get(user_id)

    if user.tipo_usuario == "empresa":
        return jsonify({"error": "Empresas não podem se candidatar em vagas"}), 403

    application = Application(
        user_id=user_id,
        job_id=job_id
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({"message": "Candidatura realizada com sucesso"})

@job_auth.route("/jobs", methods=["GET"])
def list_jobs():

    jobs = Job.query.all()

    resultado = []

    for job in jobs:
        resultado.append({
            "id": job.id,
            "titulo": job.titulo,
            "descricao": job.descricao,
            "empresa": job.empresa_id
        })

    return jsonify(resultado)