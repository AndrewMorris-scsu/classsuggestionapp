from flask.ext.wtf import Form
from wtforms import StringField


class FilterForm(Form):
    filter = StringField('filter')
