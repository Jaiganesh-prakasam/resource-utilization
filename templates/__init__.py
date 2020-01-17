from flask import Flask
app = Flask(__name__,
 static_folder = './public',
 template_folder="./static")
from templates.resource.views import cpu_blueprint
# register the blueprints
app.register_blueprint(cpu_blueprint)