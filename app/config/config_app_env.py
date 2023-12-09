from dotenv import load_dotenv
from flask import Flask
from os import environ

from app.constants import ENV_FILE


def configure_app_env(app: Flask) -> None:
    load_dotenv(ENV_FILE)
    app.config.from_mapping({
        'SECRET_KEY': environ.get('SECRET_KEY'),
    })
    