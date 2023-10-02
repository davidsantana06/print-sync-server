from datetime import datetime
from flask import Blueprint
from http import HTTPStatus
from os import listdir

from .constants import DT_FORMAT, UPLOADS_DIRECTORY
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
                'created_at': datetime.strptime(file_data[0], DT_FORMAT)
            })

    return (render_template('index', {'images': images}), HTTPStatus.OK)
