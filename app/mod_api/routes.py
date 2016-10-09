import os
from os.path import dirname


from flask import (
    session,
    render_template,
    jsonify,
    request
)
from . import api


@api.route("/fetch_data")
def handle_fetch_data():
    # class_type = request.args.get("class", "")
    data_file = os.path.join(os.getcwd(), "db", "majorcourses (1).unl")
    with open(data_file, 'r') as fh:
        data = fh.readlines()
    return jsonify(data)
