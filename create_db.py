from flask import json
from app import db
from app.mod_api.model import (
    Class,
    Major,
    Prereq,
    Requirement,
)

with open('parse/major_courses.json') as handle:
    data = json.load(handle)

    d = {}
    for cls, d in data.items():
        cls_dept = d["class_dept"]
        major_dept = d["major_dept"]
        major = d["major"]
        desc = d["description"]

        db.session.add(Class(name=cls, description=desc))
        db.session.add(Major(identifier=major, department=major_dept))
        db.session.add(Requirement(major=major, class_id=cls))
        db.session.commit()
