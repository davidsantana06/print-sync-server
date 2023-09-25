from flask_socketio import emit
from os import path
import json

from . import socket_io
from .constants import UPLOADS_FOLDER_PATH


@socket_io.on('send_capture')
def handle_message(data: str):
    try:
        message = dict(json.loads(data))
        username = message.get('username')
        send_at = message.get('send_at')
        text_message = message.get('blb_image')

        # Salvar o texto em um arquivo de texto no diretório especificado
        filename = f'{username}_{send_at}.txt'
        filepath = path.join(UPLOADS_FOLDER_PATH, filename)

        with open(filepath, 'w') as f:
            f.write(text_message)

        print(f'Mensagem recebida do cliente - Username: {username}, Send_at: {send_at}')
        emit('server_response', 'OK')
    except Exception as e:
        print(f'Erro ao processar a mensagem: {str(e)}')
        emit('server_respose', 'Erro')
