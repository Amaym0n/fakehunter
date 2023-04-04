from http import HTTPStatus

import pytest

from tests.urls import APIUrls


@pytest.mark.parametrize('status_code, username, email, password', [
    (HTTPStatus.CREATED, 'Test5', 'test@gmail.com', 'Test1'),
    (HTTPStatus.UNPROCESSABLE_ENTITY, '', 'test3@gmail.com', 'test2'),
    (HTTPStatus.UNPROCESSABLE_ENTITY, 'Test', 'test2@gmail.com', ''),
    (HTTPStatus.UNPROCESSABLE_ENTITY, {}, 'test4@gmail.com', 'test2')])
def test_user_create(client, status_code, username, email, password):
    data = {'username': username, 'email': email, 'password': password}
    response = client.post(url=APIUrls.USER.value, json=data)
    assert response.status_code == status_code, \
        f'Не получен ожидаемый статус код {status_code}. Response - {response.json()}'
