from os import path


ROOT_FOLDER = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', '..'
    )
)
UPLOADS_FOLDER = path.join(ROOT_FOLDER, 'uploads')
RESOURCES_FOLDER = path.join(ROOT_FOLDER, 'src', 'resources')
