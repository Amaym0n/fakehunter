def test_create_user(client):
    data = {'username': 'testusername', 'email': 'test@test.com', 'password': '12345678'}
    response = client.post('/users/', json=data)
    assert response.status_code == 200, f'Тест не прошел'
    assert response.json()['email'] == data['email']
    assert response.json()['username'] == data['username']
    assert response.json()['is_active']
