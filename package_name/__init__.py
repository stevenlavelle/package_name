import os

from flask import Flask, render_template

from config import config
from package_name.db import db_session

def create_app(config_name = None):
    """Create and configure an instance of the Flask application."""
    app = Flask("package_name", instance_relative_config=True)
    if config_name == None:
        config_name = os.environ.get('FLASK_ENV')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.route('/')
    def index():
        return 'hello world'

    @app.route('/home')
    def home():
        title = 'hello world'
        return render_template('home.html', title=title)

    return app
