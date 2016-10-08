from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

core = Blueprint('core', __name__, url_prefix='/')


# Set the route and accepted methods
@core.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template("core/index.html")
