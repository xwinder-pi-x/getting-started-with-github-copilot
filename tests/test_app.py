from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_signup_and_duplicate():
    email = "newstudent@mergington.edu"
    response = client.post(f"/activities/Chess Club/signup?email={email}")
    assert response.status_code == 200
    assert email in activities["Chess Club"]["participants"]

    response = client.post(f"/activities/Chess Club/signup?email={email}")
    assert response.status_code == 400


def test_signup_unknown_activity():
    response = client.post("/activities/Unknown/signup?email=a@mergington.edu")
    assert response.status_code == 404
