from flask import Blueprint, jsonify, request
from ..controllers.table_controller import TableController

table_routes = Blueprint('table_routes', __name__)

# Get all tables
@table_routes.route('/', methods=['GET', 'POST'])
def get_or_create():
    if request.method == 'GET': return jsonify({'message': 'get_tables route'})
    if request.method == 'POST': return create_account_controller()
    else: return 'Method is Not Allowed'

# Get tables per user
@table_routes.route('/user/<int:user_id>', methods=['GET'])
def get_tables_per_user(user_id):
    # update_row = content_controller.update_row(table_id, row_id) 
    # return update_row
    return jsonify({'message': 'get_tables_per_user route', 'user_id': f'{user_id}'})

@table_routes.route('/<int:table_id>', methods=['GET'])
def get_table(table_id, row_id):
    # update_row = content_controller.update_row(table_id, row_id) 
    # return update_row
    return jsonify({'message': 'get_table route', 'table_id': f'{table_id}'})

@table_routes.route('/', methods=['POST'])
def create_table():
    # update_row = content_controller.update_row(table_id, row_id) 
    # return update_row
    return jsonify({'message': 'create_table route', 'table_id': f'{table_id}'})

@table_routes.route('/update/<int:table_id>', methods=['PUT'])
def update_table(table_id):
    # update_row = content_controller.update_row(table_id, row_id) 
    # return update_row
    return jsonify({'message': 'update_table route', 'table_id': f'{table_id}'})

@table_routes.route('/delete/<int:table_id>>', methods=['DELETE'])
def delete_table(table_id):
    # delete_row = content_controller.delete_row(table_id, row_id) 
    # return delete_row
    return jsonify({'message': 'delete_table route', 'table_id': f'{table_id}'})
