from flask import Flask
from app.misc import format_dt, template


def configure_jinja_env(app: Flask) -> None:
    app.jinja_env.globals.update({
        'template': template,
        'format_dt': format_dt
    })
