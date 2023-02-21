from http import HTTPStatus


def test_create_job(client):
    data = {"title": "SDE 1 Yahoo", "company": "Yahoo", "company_url": "yahoo.com", "location": "USA, NY",
            "description": "Testing", "date_posted": "2022-07-20"}
    response = client.post(url='/job/create', json=data)
    assert response.status_code == HTTPStatus.OK, f'Got {response.status_code=}'
