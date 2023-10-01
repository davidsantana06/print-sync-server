from base64 import b64decode
from flask_socketio import emit
from os import path
import json

from .constants import UPLOADS_DIRECTORY
from .extensions import socket_io


@socket_io.on('capture')
def capture(data: str):
    response = 'OK'

    try:
        # Captar os dados enviados pelo cliente
        message = dict(json.loads(data))
        username = message.get('username')
        send_at = message.get('send_at')
        base64_image = message.get('blb_image')

        # Decodificar a string base64 para dados binários
        image_data = b64decode(base64_image)

        # Definir o nome do arquivo e o caminho para o armazenamento
        filename = f'{username} ~ {send_at}.png'
        filepath = path.join(UPLOADS_DIRECTORY, filename)

        # Salvar o arquivo no diretório do servidor.
        if not path.exists(filepath):
            with open(filepath, 'wb') as f:
                f.write(image_data)
        else:
            response = 'Image already exists'
    except Exception:
        response = 'Something is wrong with the message payload'

    emit('response', response)
