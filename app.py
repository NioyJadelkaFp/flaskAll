from flask_socketio import SocketIO
from flask import Flask, redirect, render_template, send_file, request, jsonify, session

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html', Titulo_Web='Web de Prueba')


#   Producción
#if __name__ == '__main__':
    #socketio.run(app)

#   Desarrollo
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)