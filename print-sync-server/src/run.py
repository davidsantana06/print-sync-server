from os import environ
from app import app


if __name__ == '__main__':
    app.run(
        host=environ.get('HOST'), port=environ.get('PORT'), debug=int(environ.get('DEBUG'))
    )
