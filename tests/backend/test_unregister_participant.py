from src.app import activities


def test_unregister_participant_removes_email_from_activity(client):
    activity_name = "Chess Club"
    email = "student@mergington.edu"
    activities[activity_name]["participants"].append(email)

    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"


def test_unregister_participant_returns_404_for_unknown_activity(client):
    response = client.delete("/activities/Unknown Activity/participants?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_participant_returns_404_for_unregistered_student(client):
    response = client.delete("/activities/Chess Club/participants?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not registered for this activity"}