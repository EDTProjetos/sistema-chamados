import os
import uuid
from flask import Blueprint, request, jsonify, url_for, current_app, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import cross_origin

upload_bp = Blueprint('upload', __name__)

# Configurações de upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower() if '.' in filename else ''

@upload_bp.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    try:
        # Verifica se foi enviado um arquivo
        if 'file' not in request.files:
            return jsonify({'error': 'Nenhum arquivo foi enviado'}), 400
        
        file = request.files['file']
        
        # Verifica se um arquivo foi selecionado
        if file.filename == '':
            return jsonify({'error': 'Nenhum arquivo foi selecionado'}), 400
        
        # Verifica se o arquivo é permitido
        if not allowed_file(file.filename):
            return jsonify({'error': 'Tipo de arquivo não permitido. Use: PNG, JPG, JPEG, GIF, BMP, WEBP'}), 400
        
        # Verifica o tamanho do arquivo
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)
        
        if file_size > MAX_FILE_SIZE:
            return jsonify({'error': 'Arquivo muito grande. Tamanho máximo: 16MB'}), 400
        
        # Gera um nome único para o arquivo
        file_extension = get_file_extension(file.filename)
        unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
        
        # Cria o diretório de upload se não existir
        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        os.makedirs(upload_path, exist_ok=True)
        
        # Salva o arquivo
        file_path = os.path.join(upload_path, unique_filename)
        file.save(file_path)
        
        # Gera a URL de download
        download_url = url_for('upload.download_file', filename=unique_filename, _external=True)
        
        return jsonify({
            'success': True,
            'message': 'Arquivo enviado com sucesso',
            'filename': unique_filename,
            'download_url': download_url,
            'original_filename': file.filename,
            'file_size': file_size
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Erro interno do servidor: {str(e)}'}), 500

@upload_bp.route('/download/<filename>')
@cross_origin()
def download_file(filename):
    try:
        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        return send_from_directory(upload_path, filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'Arquivo não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'Erro ao baixar arquivo: {str(e)}'}), 500

@upload_bp.route('/view/<filename>')
@cross_origin()
def view_file(filename):
    try:
        upload_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
        return send_from_directory(upload_path, filename)
    except FileNotFoundError:
        return jsonify({'error': 'Arquivo não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'Erro ao visualizar arquivo: {str(e)}'}), 500

