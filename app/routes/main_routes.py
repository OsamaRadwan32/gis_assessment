from flask import Blueprint, jsonify
from ..config.db_connect import connect_to_db
from .. import check_db_connection

from .tables_routes import table_routes
from .users_routes import user_routes
from .file_routes import file_routes
from .authentication_routes import authentication_routes

# Create a Blueprint instance
main_routes = Blueprint('main_routes', __name__)

# Define your routes
@main_routes.route('/')
def index():
    return jsonify({'message': 'Welcome to the main page'})

@main_routes.route('/dbConnect')
def normal_db_connection():
    return check_db_connection()

main_routes.register_blueprint(table_routes, url_prefix='/tables')
main_routes.register_blueprint(user_routes, url_prefix='/users')
main_routes.register_blueprint(file_routes, url_prefix='/files')
main_routes.register_blueprint(authentication_routes, url_prefix='/auth')