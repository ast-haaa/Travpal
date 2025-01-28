from flask import Flask
from app.routes import translator_bp


@translator_bp.route('/')
def home():
    return "Welcome to the Translation and Chatbot API!"

def create_app():
    app = Flask(__name__)
    app.register_blueprint(translator_bp)  # Register routes
    return app

