from http import HTTPStatus

import pytest

from tests.urls import APIUrls


@pytest.mark.parametrize('status_code, title, description, company_name, company_url, location, date_posted', [
    (HTTPStatus.CREATED, 'Python', 'New Python Job', 'Python', 'https://www.python.com/', 'Moscow', '2023-04-04'),
    (HTTPStatus.UNPROCESSABLE_ENTITY, '', 'New Python Job', 'Python', 'python.com', 'Moscow, Russia', '2023-04-04'),
    (HTTPStatus.UNPROCESSABLE_ENTITY, '5symb', '', 'Python', 'python.com', 'Moscow, Russia', '2023-04-04'),
    (HTTPStatus.CREATED, 'Python', 'Python Job', '', 'https://www.python.com/', '', '2023-04-04'),
    (HTTPStatus.UNPROCESSABLE_ENTITY, 'Python', 'Python Job', '', 'www.python.com/', '', '2023-04-04'),
    (HTTPStatus.UNPROCESSABLE_ENTITY, 'Python', 'Python Job', '', 'https://www.python.com/', '', '12.01.11')])
def test_route_job_create(client, status_code, title, description, company_url, company_name, location, date_posted):
    data = {'title': title,
            'description': description,
            'company_name': company_name,
            'company_url': company_url,
            'location': location,
            'date_posted': date_posted}
    response = client.post(url=APIUrls.JOB.value, json=data)
    assert response.status_code == status_code, \
        f'Не получен ожидаемый статус код {status_code}. Response - {response.json()}'
