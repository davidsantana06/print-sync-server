from os import path


ROOT_DIRECTORY = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', '..'
    )
)
APP_DIRECTORY = path.join(ROOT_DIRECTORY, 'src', 'app')
UPLOADS_DIRECTORY = path.join(ROOT_DIRECTORY, 'uploads')