import os
from os.path import dirname


from flask import (
    session,
    render_template,
    jsonify,
    request
)
from . import api


@api.route("/fetch_data", methods=["POST"])
def handle_fetch_data():
    class_type = request.form("data")
    print(class_type)
    data_file = os.path.join(os.getcwd(), "db", "majorcourses (1).unl")
    with open(data_file, 'r') as fh:
        data = fh.readlines()
    return jsonify(data)
