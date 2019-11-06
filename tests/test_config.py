from package_name import create_app

def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app('testing').testing

def test_index(client):
    response = client.get("/")
    assert response.data == b"hello world"
