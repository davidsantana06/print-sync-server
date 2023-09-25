from flask import render_template
from http import HTTPStatus
from werkzeug.exceptions import HTTPException

from . import app
from .utils import render_page


@app.errorhandler(Exception)
def error_handler(e: Exception):
    e_code = e.code if (isinstance(e, HTTPException)) else 500
    description = 'Oops! Página não encontrada.' if e_code == 404 else 'Oops! Algo deu errado.'
    http_status = HTTPStatus(e_code)
    data = {
        'error': {
            'code': e_code,
            'description': description
        }
    }

    return (render_page('error-handler', data), http_status)


@app.get('/')
def index():
    return (render_page('index'), HTTPStatus.OK)
