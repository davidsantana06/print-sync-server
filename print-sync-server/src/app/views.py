from datetime import datetime
from flask import (
    Blueprint,
    abort, send_file
)
from http import HTTPStatus
from os import (
    path,
    listdir
)

from .constants import DT_FORMAT, IMAGE_EXTENSION, UPLOADS_DIRECTORY
from .misc import render_template


main = Blueprint('main', __name__)


@main.get('/')
def index():
    images = []

    for file_name in listdir(UPLOADS_DIRECTORY):
        file_data = file_name.split(' ~ ')

        if len(file_data) == 2:
            images.append({
                'author': file_data[-1].split('.')[0],
                'created_at': datetime.strptime(file_data[0], DT_FORMAT),
                'file_name': file_name
            })

    return (render_template('index', {'images': images}), HTTPStatus.OK)


@main.get('/uploads/<file_name>')
def uploads(file_name: str):
    image = path.join(UPLOADS_DIRECTORY, file_name)

    if path.exists(image):
        response = send_file(image, as_attachment=True), HTTPStatus.OK
    else:
        abort(404)
    
    return response