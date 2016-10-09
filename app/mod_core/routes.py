from flask import render_template
from . import core


@core.route('/', methods=['GET', 'POST'])
def index():
    return render_template("core/index.html")
