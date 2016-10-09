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

    name = db.Column(db.String, nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return "stuff"


class Dependencies(Base):
    __tablename__ = "Dependencies"

    class_id = db.Column(db.Integer, db.ForeignKey(Class.id))

    def __init__(self):
        pass


class Prereq(Base):
    __tablename__ = "Prereq"

    def __init__(self):
        pass


class Major(Base):
    __tablename__ = "Major"

    def __init__(self):
        pass
