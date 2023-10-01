from flask import Flask
from http import HTTPStatus
from werkzeug.exceptions import HTTPException

from app.misc import render_template


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

    return (render_template('error-handler', data), http_status)


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, error_handler)
