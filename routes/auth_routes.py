from flask import Blueprint, request, jsonify
from models import User
from database import db
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")
    tipo_usuario = data.get("tipo_usuario")

    senha_hash = generate_password_hash(senha)

    user = User(
        nome = nome,
        email = email,
        senha = senha_hash,
        tipo_usuario = tipo_usuario
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuário cadastrado com sucesso"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    senha = data.get("senha")

    user = User.query.filter_by(email=email).first()

    if not email or not senha:
        return jsonify({"message": "Por favor, preencha todos os campos"})
    

    if not user:
        return jsonify({"error": "Nenhum usuário encontrado"}), 404
    
    if not check_password_hash(user.senha, senha):
        return jsonify({"error": "Senha inválida"}), 401
    
    token = create_access_token(identity=str(user.id))

    return jsonify({
        "message": "Login realizado",
        "token": token
    })