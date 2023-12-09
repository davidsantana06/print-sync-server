from flask import Flask
from app.extensions import socket_io


def configure_extensions(app: Flask) -> None:
    socket_io.init_app(
        app, cors_allowed_origins='*', websocket_max_message_size=10 * 1024 * 1024
    )
