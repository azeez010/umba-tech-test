class TestUser:
    def test_create_user(self, app, client):
        response = client.post("/api/v1/user/", data={
            "email": "azeez1@gmail.com",
            "password": "azeezlab",
            "first_name": "hello",
            "last_name": "hi",
            "phone_number": "09123456789"
        })
        assert response.status_code == 200

    def test_retrieve_user(self, app, user, login, client):
        response = client.get("/api/v1/user/%s" % user.get("id"), headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 200

    def test_update_user(self, app, user, login, client):
        response = client.put("/api/v1/user/%s" % user.get("id"), data={"first_name": "adam"}, headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 200

    def test_delete_user(self, app, user, login, client):
        response = client.delete("/api/v1/user/%s" % user.get("id"), headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 204

    def test_list_users(self, app, user, login, client):
        response = client.get("/api/v1/user/", headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 200
