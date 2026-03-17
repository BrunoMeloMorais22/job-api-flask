from flask import Flask
from database import db
from models import User, Job, Application
from config import Config
import os
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from routes.job_routes import job_auth

app = Flask(__name__)


app.config.from_object(Config)


database_url = os.environ.get('DATABASE_URL')

if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(job_auth)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "API de Gerenciador de Tarefas",
        "endpoints": {
            "register": "POST /register",
            "login": "POST /login",
            "criar_vaga": "POST /job",
            "Candidatar-se": "POST /jobs/<int:job_id>/apply",
            "Listar": "GET /jobs"
        }}

if __name__ == "__main__":
    app.run(debug=True)