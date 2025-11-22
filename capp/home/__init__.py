from flask import Blueprint

# Création du Blueprint
home = Blueprint('home', __name__)

# Import des routes pour que Flask les connaisse
from . import routes
