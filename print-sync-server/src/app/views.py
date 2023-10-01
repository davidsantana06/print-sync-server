from flask import Blueprint
from http import HTTPStatus

from .misc import render_template


main = Blueprint('main', __name__)


@main.get('/')
def index():
    return (render_template('index'), HTTPStatus.OK)
