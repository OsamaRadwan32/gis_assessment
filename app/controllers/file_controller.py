""" file_controller.py """

from flask import jsonify
# from ..models.dynamic_table_model import DynamicTable
from .table_controller import TableController
from ..services.table_services import TableServices
from ..services.file_services import FileServices

class FileController:
    """
    File Controller class
    """
    @staticmethod
    def process_request(request):
        """
        Adds two numbers and returns the result.

        Parameters:
            request object containing the following attributes:
                - table_name (str): the name of the table to create.
                - table_structure (json): the table structure in json format.
                - file_name (str): the name of the uploaded file.
                - file(file): the actual up loaded file.
        """
        request_form = request.form.to_dict()
        table_name = request_form['table_name']
        table_structure = request_form['table_structure']
        db_table_name = TableServices.generate_tablename(3, table_name)
        try:    
            # check if there is a record with the same table name in the 'tables' table
            # and if their is a table holding the db_table_name existing in the database
            table_record_exists = TableServices.check_tablename_record(3, db_table_name)
            table_exists = TableServices.check_table_exists(db_table_name)
            if table_record_exists or table_exists:
                return jsonify({"error": "Table already exists in the database. Choose another name"}), 400  
            # Check if the uploaded file exists and has a CSV extension
            file = request.files['file']
            file_name = file.filename
            check_filename = FileServices.allowed_file_extensions(file_name)
            if 'file' not in request.files or not check_filename:
                return jsonify({'error': 'No selected file or wrong file extension!'}), 400
            # Generate a file name and save the file in the static/tables folder
            upload_file = FileServices.save_uploaded_file(db_table_name, file)
            # Creating a record of the table info in the 'tables' table
            TableServices.add_table_info(db_table_name, 3, table_structure, upload_file[64:])                
            TableController.create_table_in_db(db_table_name, table_structure)            
            TableController.populate_table(db_table_name, table_structure, upload_file)
            return jsonify({'message': f'Table {table_name} created and populated successfully'}), 200
        except Exception as e:
            # Handle the exception and return a custom response
            error_message = str(e)
            return jsonify({"error": error_message}), 500  
