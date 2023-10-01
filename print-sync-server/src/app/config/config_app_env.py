from dotenv import load_dotenv
from flask import Flask
from os import environ, path

from app.constants import ROOT_DIRECTORY


ENV_FILE_PATH = path.join(ROOT_DIRECTORY, '..', '.env')
load_dotenv(ENV_FILE_PATH)


def configure_app_env(app: Flask) -> None:
    app.config.from_mapping({
        'SECRET_KEY': environ.get('SECRET_KEY'),
    })
    