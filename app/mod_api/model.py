from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date_created = db.Column(db.DateTime,
                             default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
                              default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Class(Base):
    __tablename__ = "Class"

    name = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text)

    prereqs = db.relationship(
        "Prereq", cascade="save-update, merge, delete")

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return "stuff"


class Prereq(Base):
    __tablename__ = "Prereq"

    class_id = db.Column(db.Integer, db.ForeignKey(Class.id))
    prereq = db.Column(db.Integer)

    def __init__(self, src=None, target=None):
        self.class_src_id = src
        self.class_target_id = target


class Major(Base):
    __tablename__ = "Major"

    department = db.Column(db.Text, nullable=False)
    identifier = db.Column(db.Text, nullable=False)

    requirements = db.relationship(
        "Requirement", cascade="save-update, merge, delete")

    def __init__(self, department=None, identifier=None):
        self.department = department
        self.identifier = identifier


class Requirement(Base):
    __tablename__ = "Requirement"

    major_id = db.Column(db.Integer, db.ForeignKey(Major.id), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey(Class.id), nullable=False)

    def __init__(self, major=None, class_id=None):
        self.major_id = major
        self.class_id = class_id
