from flask import Blueprint

users_bp = Blueprint('users_bp', __name__)

# Import routes here to avoid circular imports
from . import routes
