import os

from flask import Flask, render_template
from config import config

config_name = os.environ.get('FLASK_ENV')

def create_app(config_name = 'default'):
    """Create and configure an instance of the Flask application."""
    app = Flask("package_name", instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'hello world'

    @app.route('/home')
    def home():
        title = 'hello world'
        return render_template('home.html', title=title)

    return app
