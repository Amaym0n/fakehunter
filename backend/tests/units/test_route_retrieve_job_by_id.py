from http import HTTPStatus

import pytest

from tests.urls import APIUrls


@pytest.mark.parametrize('status_code, job_id', [(HTTPStatus.NOT_FOUND, 1),
                                                 (HTTPStatus.UNPROCESSABLE_ENTITY, 'x'),
                                                 (HTTPStatus.UNPROCESSABLE_ENTITY, ''),
                                                 (HTTPStatus.UNPROCESSABLE_ENTITY, ' '),
                                                 (HTTPStatus.UNPROCESSABLE_ENTITY, -1),
                                                 (HTTPStatus.NOT_FOUND, '1')])
def test_route_retrieve_job_by_id(client, status_code, job_id):
    response = client.get(url=APIUrls.JOB.value, params={'job_id': job_id})
    assert response.status_code == status_code, \
        f'Полученный status_code {response.status_code} не соответствует ожидаемому {status_code}'
