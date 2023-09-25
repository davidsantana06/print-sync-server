from flask_socketio import emit
from . import socket_io


@socket_io.on('mensagem_do_cliente')
def handle_message(message):
    print(f'Mensagem recebida do cliente: {message}')
    emit('resposta_do_servidor', 'OK')
