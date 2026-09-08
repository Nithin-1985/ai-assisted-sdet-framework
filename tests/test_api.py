import requests
BASE_URL = "https://jsonplaceholder.typicode.com"



def test_get_existing_user():
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["email"] == "Sincere@april.biz"


def test_get_non_existing_user():
    response = requests.get(f"{BASE_URL}/users/999")

    assert response.status_code == 404

    body = response.json()

    assert body == {}


def test_create_user():
    payload = {
        "name": "Nithin",
        "username": "nithinp",
        "email": "nithin@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload
    )

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Nithin"
    assert body["username"] == "nithinp"
    assert body["email"] == "nithin@example.com"
    assert "id" in body

    


def test_update_user():

    payload = {
        "name": "Nithin Updated",
        "username": "nithinp",
        "email": "nithin.updated@example.com"
    }

    response = requests.put(
        f"{BASE_URL}/users/1",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == "Nithin Updated"
    assert body["username"] == "nithinp"
    assert body["email"] == "nithin.updated@example.com"
    assert body["id"] == 1