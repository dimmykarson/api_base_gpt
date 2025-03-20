from app.routes import bp
import os
from flask import request, jsonify

from app.services.document_analysis_deepseek import extract_document_metadata
from app.services.document_analysis_gpt import extract_document_metadata_gpt
from app.utils.file_utils import allowed_file


UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route('/')
def index():
    return 'Hello, World!'


@bp.route('/analise', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nome do arquivo inválido'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'Apenas arquivos PDF são permitidos'}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    metadata = extract_document_metadata(file_path)

    return jsonify(metadata), 200


@bp.route('/analise/gpt', methods=['POST'])
def upload_file_gpt():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nome do arquivo inválido'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'Apenas arquivos PDF são permitidos'}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    metadata = extract_document_metadata_gpt(file_path)

    return jsonify(metadata), 200
