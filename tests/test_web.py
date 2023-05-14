"""
Pytest for web/__init__.py
which starts the front-end
"""


def test_index(app, client):
    res = client.get("/")
    assert res.status_code == 200


def test_simple_correct_data(app, client):
    res = client.get("/simple")
    assert res.status_code == 200
    assert b"Simple Authentication" in res.data

    with client.session_transaction() as session:
        this_code = session["simple_val"]
        res = client.post("/simple_authentication", data={"authentication": this_code})
        assert res.status_code == 200


def test_simple_incorrect_data(app, client):
    res = client.get("/simple")
    assert res.status_code == 200
    assert b"Simple Authentication" in res.data

    with client.session_transaction() as session:
        this_code = "BADCODE"  # Pass a value that isn't the correct authentication code
        assert this_code != session["simple_val"]
        res = client.post("/simple_authentication", data={"authentication": this_code})
        assert res.status_code == 302


def test_simple_authentication_endpoint(app, client):
    res = client.get("/simple_authentication")
    # The default should make this inaccessible
    # This only should be sent info and then evaluate it
    assert res.status_code == 405


# ---- Hard ----


def test_hard_correct_data(app, client):
    res = client.get("/hard")
    assert res.status_code == 200
    assert b"Hard Authentication" in res.data

    with client.session_transaction() as session:
        this_code = session["hard_val"]
        res = client.post("/hard_authentication", data={"authentication": this_code})
        assert res.status_code == 200


def test_hard_incorrect_data(app, client):
    res = client.get("/hard")
    assert res.status_code == 200
    assert b"Hard Authentication" in res.data

    with client.session_transaction() as session:
        this_code = "BADCODE"  # Pass a value that isn't the correct authentication code
        assert this_code != session["hard_val"]
        res = client.post("/hard_authentication", data={"authentication": this_code})
        assert res.status_code == 302


def test_hard_authentication_endpoint(app, client):
    res = client.get("/hard_authentication")
    # The default should make this inaccessible
    # This only should be sent info and then evaluate it
    assert res.status_code == 405


# ---- Hardest ----
def test_hardest_correct_data(app, client):
    res = client.get("/hardest")
    assert res.status_code == 200
    assert b"Hardest Authentication" in res.data

    with client.session_transaction() as session:
        this_code = session["hardest_val"]
        res = client.post("/hardest_authentication", data={"authentication": this_code})
        assert res.status_code == 200


def test_hardest_incorrect_data(app, client):
    res = client.get("/hardest")
    assert res.status_code == 200
    assert b"Hardest Authentication" in res.data

    with client.session_transaction() as session:
        this_code = "BADCODE"  # Pass a value that isn't the correct authentication code
        assert this_code != session["hardest_val"]
        res = client.post("/hardest_authentication", data={"authentication": this_code})
        assert res.status_code == 302


def test_hardest_authentication_endpoint(app, client):
    res = client.get("/hardest_authentication")
    # The default should make this inaccessible
    # This only should be sent info and then evaluate it
    assert res.status_code == 405
