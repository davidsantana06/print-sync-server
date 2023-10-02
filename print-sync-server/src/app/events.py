from base64 import b64decode
from datetime import datetime
from flask_socketio import emit
from os import path
import json

from .constants import DT_FORMAT, IMAGE_EXTENSION, UPLOADS_DIRECTORY
from .extensions import socket_io


@socket_io.on('capture')
def capture(data: str):
    response = 'OK'

    try:
        # Captar os dados enviados pelo cliente
        message = dict(json.loads(data))
        author = message.get('username')
        created_at = message.get('send_at')
        base64_image = message.get('blb_image')

        # Transformar a data em um objeto datetime
        created_at = datetime.strptime(created_at, DT_FORMAT)

        # Decodificar a string base64 para dados binários
        image_data = b64decode(base64_image)

        # Definir o nome do arquivo e o caminho para o armazenamento
        filename = f'{created_at} ~ {author}.{IMAGE_EXTENSION}'
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
