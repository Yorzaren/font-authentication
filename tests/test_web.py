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
    assert b"Simple Validation" in res.data

    with client.session_transaction() as session:
        this_code = session["simple_val"]
        res = client.post("/simple_validation", data={"validation": this_code})
        assert res.status_code == 200


def test_simple_incorrect_data(app, client):
    res = client.get("/simple")
    assert res.status_code == 200
    assert b"Simple Validation" in res.data

    with client.session_transaction() as session:
        this_code = "BADCODE"  # Pass a value that isn't the correct validation code
        assert this_code != session["simple_val"]
        res = client.post("/simple_validation", data={"validation": this_code})
        assert res.status_code == 302


def test_simple_validation_endpoint(app, client):
    res = client.get("/simple_validation")
    # The default should make this inaccessible
    # This only should be sent info and then evaluate it
    assert res.status_code == 405


# ---- Hard ----


def test_hard_correct_data(app, client):
    res = client.get("/hard")
    assert res.status_code == 200
    assert b"Harder Validation" in res.data

    with client.session_transaction() as session:
        this_code = session["hard_val"]
        res = client.post("/hard_validation", data={"validation": this_code})
        assert res.status_code == 200


def test_hard_incorrect_data(app, client):
    res = client.get("/hard")
    assert res.status_code == 200
    assert b"Harder Validation" in res.data

    with client.session_transaction() as session:
        this_code = "BADCODE"  # Pass a value that isn't the correct validation code
        assert this_code != session["hard_val"]
        res = client.post("/hard_validation", data={"validation": this_code})
        assert res.status_code == 302


def test_hard_validation_endpoint(app, client):
    res = client.get("/hard_validation")
    # The default should make this inaccessible
    # This only should be sent info and then evaluate it
    assert res.status_code == 405


# ---- Hardest ----
def test_hardest_correct_data(app, client):
    res = client.get("/hardest")
    assert res.status_code == 200
    assert b"Hardest Validation" in res.data

    with client.session_transaction() as session:
        this_code = session["hardest_val"]
        res = client.post("/hardest_validation", data={"validation": this_code})
        assert res.status_code == 200


def test_hardest_incorrect_data(app, client):
    res = client.get("/hardest")
    assert res.status_code == 200
    assert b"Hardest Validation" in res.data

    with client.session_transaction() as session:
        this_code = "BADCODE"  # Pass a value that isn't the correct validation code
        assert this_code != session["hardest_val"]
        res = client.post("/hardest_validation", data={"validation": this_code})
        assert res.status_code == 302


def test_hardest_validation_endpoint(app, client):
    res = client.get("/hardest_validation")
    # The default should make this inaccessible
    # This only should be sent info and then evaluate it
    assert res.status_code == 405
