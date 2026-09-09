



def test_get_existing_user(api_client):
    response = api_client.get_user(1)

    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["email"] == "Sincere@april.biz"


def test_get_non_existing_user(api_client):
    response = api_client.get_user(999)

    assert response.status_code == 404

    body = response.json()

    assert body == {}


def test_create_user(api_client):
    payload = {
        "name": "Nithin",
        "username": "nithinp",
        "email": "nithin@example.com"
    }

    response = api_client.create_user(payload)

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Nithin"
    assert body["username"] == "nithinp"
    assert body["email"] == "nithin@example.com"
    assert "id" in body

    


def test_update_user(api_client):

    payload = {
        "name": "Nithin Updated",
        "username": "nithinp",
        "email": "nithin.updated@example.com"
    }

    response = api_client.update_user(1, payload)

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == "Nithin Updated"
    assert body["username"] == "nithinp"
    assert body["email"] == "nithin.updated@example.com"
    assert body["id"] == 1

def test_delete_user(api_client):

    response = api_client.delete_user(1)

    assert response.status_code == 200

    body = response.json()
    assert body == {}