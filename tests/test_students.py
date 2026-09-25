import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest

from src import create_app
from src.data import data


@pytest.fixture
def client():
    data.reset_data()
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_all_students(client):
    resp = client.get("/students")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) == 5


def test_get_student_by_id(client):
    resp = client.get("/students")
    student_id = resp.get_json()[0]["id"]
    resp = client.get(f"/students/{student_id}")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["id"] == student_id


def test_get_student_not_found(client):
    resp = client.get("/students/99999")
    assert resp.status_code == 404


def test_get_all_students_after_delete(client):
    resp = client.get("/students")
    student_id = resp.get_json()[2]["id"]
    client.delete(f"/students/{student_id}")
    resp = client.get("/students")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 4


def test_get_student_fields(client):
    resp = client.get("/students")
    student = resp.get_json()[0]
    assert "id" in student
    assert "firstName" in student
    assert "lastName" in student
    assert "email" in student
    assert "grade" in student


def test_create_student(client):
    data = {"firstName": "Ari", "lastName": "Gato", "email": "ari.gato@test.fr", "grade": 16.0}
    resp = client.post("/students", json=data)
    assert resp.status_code == 201
    created = resp.get_json()
    assert created["firstName"] == "Ari"
    assert "id" in created


def test_create_student_missing_fields(client):
    data = {"firstName": "Bob"}
    resp = client.post("/students", json=data)
    assert resp.status_code == 400


def test_create_student_no_body(client):
    resp = client.post("/students")
    assert resp.status_code == 400


def test_create_student_default_grade(client):
    data = {"firstName": "Charlie", "lastName": "Petit", "email": "charlie.petit@test.fr"}
    resp = client.post("/students", json=data)
    assert resp.status_code == 201
    assert resp.get_json()["grade"] == 0


def test_update_student(client):
    resp = client.get("/students")
    student_id = resp.get_json()[0]["id"]
    data = {"firstName": "Jean-Pierre"}
    resp = client.put(f"/students/{student_id}", json=data)
    assert resp.status_code == 200
    resp = client.get(f"/students/{student_id}")
    assert resp.get_json()["firstName"] == "Jean-Pierre"


def test_update_student_not_found(client):
    resp = client.put("/students/99999", json={})
    assert resp.status_code == 404


def test_delete_student(client):
    resp = client.get("/students")
    student_id = resp.get_json()[0]["id"]
    resp = client.delete(f"/students/{student_id}")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Étudiant supprimé"


def test_delete_student_not_found(client):
    resp = client.delete("/students/99999")
    assert resp.status_code == 404


def test_stats(client):
    resp = client.get("/students/stats")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "total" in data
    assert "averageGrade" in data
    assert data["total"] == 5


def test_search_students(client):
    resp = client.get("/students/search?q=Marley")
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data) >= 1
    assert data[0]["lastName"].lower() == "marley"


def test_search_no_query(client):
    resp = client.get("/students/search")
    assert resp.status_code == 400
