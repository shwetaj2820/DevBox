from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

db_user = os.getenv("POSTGRES_USER", "postgres")
db_password = os.getenv("POSTGRES_PASSWORD", "password")
db_name = os.getenv("POSTGRES_DB", "devbox")
db_host = os.getenv("POSTGRES_HOST", "devbox-postgres")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False 
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

@app.route("/")
def home():
    return jsonify({
        "message":"DevBox API",
        "database_host": db_host
    })

@app.route("/health")
def health():
    try:
        db.session.execute(db.text("SELECT 1"))
        return jsonify({
            "status":"healthy",
            "database":"connected"
        })

    except Exception as e:
        return jsonify({
            "status":"unhealthy",
            "error":str(e)
        }),500

with app.app_context():
    db.create_all()

app.run(host="0.0.0.0", port=5000)