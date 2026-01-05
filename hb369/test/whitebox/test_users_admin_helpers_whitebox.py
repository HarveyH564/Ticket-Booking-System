import Users
import pytest


@pytest.fixture
def isolated_users_dir(tmp_path, monkeypatch):
    test_dir = tmp_path / "users"
    test_dir.mkdir()
    monkeypatch.setattr(Users, "USERS_DIR", str(test_dir))
    return test_dir


def test_branch_update_user_old_exists_true(isolated_users_dir):
    Users.create_user("alice", "p")
    assert Users.update_user("alice", "alice", "p2") is True


def test_branch_update_user_old_exists_false(isolated_users_dir):
    assert Users.update_user("missing", "x", "p") is False


def test_branch_update_user_rename_collision_true(isolated_users_dir):
    Users.create_user("alice", "p")
    Users.create_user("bob", "p")
    # new_username != old_username AND user_exists(new_username) => False path return
    assert Users.update_user("alice", "bob", "p2") is False


def test_branch_update_user_rename_collision_false(isolated_users_dir):
    Users.create_user("alice", "p")
    # new_username != old_username AND user_exists(new_username) == False => allowed
    assert Users.update_user("alice", "carol", "p2") is True
