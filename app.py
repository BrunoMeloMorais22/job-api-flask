from flask import Flask
from database import db
from models import User, Job, Application
from config import Config
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from routes.job_routes import job_auth

app = Flask(__name__)

jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(job_auth)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "API de Vagas de Emprego"}

if __name__ == "__main__":
    app.run(debug=True)