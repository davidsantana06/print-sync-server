from flask import Flask, Blueprint
from importlib import import_module
from os import listdir

from app.constants import APP_DIRECTORY


EVENTS_PACKAGE = 'app.events'
VIEWS_PACKAGE = 'app.views'


def configure_module(app: Flask) -> None:
    package_items = listdir(APP_DIRECTORY)

    for package in package_items:
        if package == 'events.py':
            import_module(EVENTS_PACKAGE)

        if package == 'views.py':
            views = import_module(VIEWS_PACKAGE)

            for _, item in views.__dict__.items():
                if isinstance(item, Blueprint):
                    app.register_blueprint(item)
                    break
