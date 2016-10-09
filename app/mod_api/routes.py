import os
from flask import (
    render_template,
    jsonify,
    request
)
from . import api
from app.mod_api.model import (
    db,
    Class,
    Major
)


@api.route("/fetch_data")
def handle_fetch_data():
    class_type = request.args.get("data")
    print(class_type)
    data_file = os.path.join(os.getcwd(), "db", "majorcourses (1).unl")
    with open(data_file, 'r') as fh:
        data = fh.readlines()
    return jsonify(data)


@api.route("/fetch_major_count")
def handle_fetch_major_count():
    major = request.args.get("data")
    count = db.session.query(Major.identifier).filter(
        Major.identifier == major).count()
    return jsonify(count)


@api.route("/fetch_majors")
def handle_fetch_majors():
    majors = []
    for major in db.session.query(Major.identifier).distinct():
        majors.append(major.identifier)
    return jsonify(majors)
