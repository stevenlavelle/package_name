import os
import tempfile

import pytest

from package_name import create_app


@pytest.fixture
def app():
    # create the app - add configuration
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
