from api_Calendar.resources.eventResources import EVENTS_ENDPOINT

def test_events_post(client):
    new_event_json = {"title": "Doctor", "description": "see results", "start_date": "2022-11-03T00:00:00", "end_date": "2022-11-03T00:00:01"}
    response = client.post(f"{EVENTS_ENDPOINT}", json=new_event_json)
    assert response.status_code == 201


def test_events_post_error(client):
    missing_pos_json = {"title": "go to the doctor"}
    response = client.post(f"{EVENTS_ENDPOINT}", json=missing_pos_json)
    assert response.status_code == 400


def test_get_all_events(client):
    response = client.get(f"{EVENTS_ENDPOINT}")
    assert response.status_code == 200
    

def test_get_single_events(client):
    response = client.get(f"{EVENTS_ENDPOINT}/1")
    assert response.status_code == 200


def test_get_single_events_not_found(client):
    response = client.get(f"{EVENTS_ENDPOINT}/55")
    assert response.status_code == 404

def test_events_put(client):
    new_event_json = {"title": "Go to the Doctor", "description": "see results", "start_date": "2022-11-03T00:00:00", "end_date": "2022-11-03T00:00:01"}
    response = client.put(f"{EVENTS_ENDPOINT}/1", json=new_event_json)
    assert response.status_code == 201


def test_events_put_error(client):
    missing_put_json = {"title": "go to the doctor"}
    response = client.put(f"{EVENTS_ENDPOINT}/55", json=missing_put_json)
    assert response.status_code == 404

def test_delete_events(client):
    response = client.delete(f"{EVENTS_ENDPOINT}/1")

    assert response.status_code == 204

def test_delete_events_error(client):
    response = client.delete(f"{EVENTS_ENDPOINT}/55")

    assert response.status_code == 404    
    
