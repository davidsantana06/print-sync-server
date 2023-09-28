from app import app, socket_io


if __name__ == '__main__':
    socket_io.run(app, host='25.62.141.82', port=5000, debug=True)
