from os import path


ROOT_FOLDER_PATH = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', '..'
    )
)
UPLOADS_FOLDER_PATH = path.join(ROOT_FOLDER_PATH, 'uploads')
RESOURCES_FOLDER_PATH = path.join(ROOT_FOLDER_PATH, 'src', 'resources')
