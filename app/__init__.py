from flask import Flask, render_template
from app.core.controllers import core as core_module

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

app.register_blueprint(core_module)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


app.register_blueprint(core_module)
