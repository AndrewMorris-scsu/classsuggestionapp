from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

# Define the WSGI application object
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
socketio = SocketIO(app)

from .mod_core import core as core_module
from .mod_api import api as api_module

# Configurations
app.register_blueprint(core_module)
app.register_blueprint(api_module)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


app.register_blueprint(core_module)
app.register_blueprint(api_module)

db.create_all()
