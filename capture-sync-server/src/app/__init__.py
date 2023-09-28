from flask import Flask
from flask_socketio import SocketIO
from os import path

from .constants import RESOURCES_FOLDER
from .utils import component, dt_now, layout, format_dt


app = Flask(__name__)
socket_io = SocketIO(app, cors_allowed_origins='*', websocket_max_message_size=10 * 1024 * 1024)

app.static_folder = path.join(RESOURCES_FOLDER, 'static')
app.template_folder = path.join(RESOURCES_FOLDER, 'templates')
app.jinja_env.globals.update({
    'component': component,
    'layout': layout,
    'dt_now': dt_now,
    'format_dt': format_dt
})


from .events import *
from .views import *
