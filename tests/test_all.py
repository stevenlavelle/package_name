import pytest
import package_name

def test_app_startup():
    assert package_name.app is not None
