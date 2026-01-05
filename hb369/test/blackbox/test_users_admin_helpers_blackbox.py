import json
import os
import pytest
import Users


@pytest.fixture
def isolated_users_dir(tmp_path, monkeypatch):
    """
    Redirect Users.USERS_DIR to a temporary folder so tests never touch real users/.
    """
    test_dir = tmp_path / "users"
    test_dir.mkdir()
    monkeypatch.setattr(Users, "USERS_DIR", str(test_dir))
    return test_dir


# ---------- create_user ----------
def test_create_user_success(isolated_users_dir):
    ok = Users.create_user("alice", "pass")
    assert ok is True
    assert Users.user_exists("alice") is True

    data = Users.load_user("alice")
    assert data["username"] == "alice"
    assert data["password"] == "pass"
    assert data["tickets"] == {}
    assert data["cart"] == {}


@pytest.mark.parametrize("username,password", [
    ("", "pass"),       # empty username
    ("alice", ""),      # empty password
    (None, "pass"),     # None username
    ("alice", None),    # None password
])
def test_create_user_rejects_missing_fields(isolated_users_dir, username, password):
    ok = Users.create_user(username, password)
    assert ok is False


def test_create_user_rejects_duplicate(isolated_users_dir):
    assert Users.create_user("alice", "pass") is True
    assert Users.create_user("alice", "pass2") is False


# ---------- list_all_users ----------
def test_list_all_users_empty(isolated_users_dir):
    assert Users.list_all_users() == []


def test_list_all_users_sorted(isolated_users_dir):
    Users.create_user("charlie", "p")
    Users.create_user("alice", "p")
    Users.create_user("bob", "p")
    assert Users.list_all_users() == ["alice", "bob", "charlie"]


# ---------- load_user ----------
def test_load_user_nonexistent_returns_none(isolated_users_dir):
    assert Users.load_user("ghost") is None


# ---------- delete_user ----------
def test_delete_user_success(isolated_users_dir):
    Users.create_user("alice", "pass")
    assert Users.delete_user("alice") is True
    assert Users.user_exists("alice") is False


def test_delete_user_nonexistent(isolated_users_dir):
    assert Users.delete_user("ghost") is False


# ---------- update_user ----------
def test_update_user_change_password_only(isolated_users_dir):
    Users.create_user("alice", "old")
    ok = Users.update_user("alice", "alice", "new")
    assert ok is True
    data = Users.load_user("alice")
    assert data["username"] == "alice"
    assert data["password"] == "new"


def test_update_user_rename_success(isolated_users_dir):
    Users.create_user("alice", "pass")
    ok = Users.update_user("alice", "alice2", "pass2")
    assert ok is True

    assert Users.user_exists("alice") is False
    assert Users.user_exists("alice2") is True

    data = Users.load_user("alice2")
    assert data["username"] == "alice2"
    assert data["password"] == "pass2"


def test_update_user_rejects_old_missing(isolated_users_dir):
    ok = Users.update_user("ghost", "newname", "p")
    assert ok is False


def test_update_user_rejects_rename_to_existing(isolated_users_dir):
    Users.create_user("alice", "p")
    Users.create_user("bob", "p")
    ok = Users.update_user("alice", "bob", "newp")
    assert ok is False
