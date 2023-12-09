from flask import Flask
from importlib import import_module

from .config import configure_app_env, configure_error_handler, configure_extensions, configure_jinja_env


app = Flask(__name__)

configure_app_env(app)
configure_error_handler(app)
configure_extensions(app)
configure_jinja_env(app)

import_module('app.events')
import_module('app.views')
