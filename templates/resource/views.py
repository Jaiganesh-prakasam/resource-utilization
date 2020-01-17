from flask import render_template, Blueprint
cpu_blueprint = Blueprint('cpu',__name__)
@hello_blueprint.route('/')
@hello_blueprint.route('/resource')
def index():
 return render_template("index.html")