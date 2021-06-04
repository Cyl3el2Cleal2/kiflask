import os
import imghdr
import uuid
from flask import Flask, request
from flask.helpers import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from werkzeug.utils import secure_filename
from flask_cors import CORS
# from flask_jwt_extended import JWTManager

from controllers.index import initial_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{username}:{password}@{host}/{db}'.format(
    username='root', password='example', host='localhost', db='kiflask')
# Image Config
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg','.jpeg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'img/'

# CORS
CORS(app)

# connect DB
db = SQLAlchemy(app)

# RestAPI Instant
api = Api(app)

# Apply Routes
initial_routes(api)

# Upload photo
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/uploads/img', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(str(uuid.uuid4())+uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return "Invalid image", 400
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return {'filename': filename}, 201

@app.route('/img/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

# Rollback when db fail
@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
