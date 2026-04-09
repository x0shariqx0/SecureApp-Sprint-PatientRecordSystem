from app import create_app

def test_app_creation():
    app = create_app()
    assert app is not None

def test_home_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code in [200, 302]
