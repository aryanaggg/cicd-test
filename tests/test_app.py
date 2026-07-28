from app.app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    # assert response.json["message"] == "Hello CI/CD!"
    assert response.json["message"] == "Hello, We are LIVE!"


# def test_health():
#     client = app.test_client()
#     response = client.get("/health")
#     assert response.status_code == 200
#     assert response.json["message"] == "Healthy"
