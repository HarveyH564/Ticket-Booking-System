import Users
import pytest


@pytest.fixture
def isolated_users_dir(tmp_path, monkeypatch):
    """
    Redirect Users.USERS_DIR to a temporary folder so tests never touch real users/.
    """
    test_dir = tmp_path / "users"
    test_dir.mkdir()
    monkeypatch.setattr(Users, "USERS_DIR", str(test_dir))
    return test_dir


def test_update_user_concolic_sequence(isolated_users_dir):
    """
    Concolic idea:
    Start with a concrete input that succeeds, then mutate inputs to flip each branch condition.

    Branches in Users.update_user(old, new, pw):
      1) if not user_exists(old): return False
      2) if new != old and user_exists(new): return False
      3) otherwise: return True and update/rename
    """

    # Concrete start: make E_old = True, R = False  -> success
    assert Users.create_user("alice", "p1") is True
    assert Users.update_user("alice", "alice", "p2") is True
    assert Users.load_user("alice")["password"] == "p2"

    # Mutate to flip R = True and keep E_new = False -> rename success (still path 3)
    assert Users.update_user("alice", "carol", "p3") is True
    assert Users.user_exists("alice") is False
    assert Users.user_exists("carol") is True
    assert Users.load_user("carol")["username"] == "carol"
    assert Users.load_user("carol")["password"] == "p3"

    # Mutate to force collision: set E_new = True while R = True -> fail (path 2)
    assert Users.create_user("bob", "pb") is True
    assert Users.update_user("carol", "bob", "p4") is False

    # Mutate to force missing old user: E_old = False -> fail (path 1)
    assert Users.update_user("ghost", "x", "p") is False
