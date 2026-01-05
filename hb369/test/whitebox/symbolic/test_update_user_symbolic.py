import pytest
import Users


@pytest.fixture
def isolated_users_dir(tmp_path, monkeypatch):
    test_dir = tmp_path / "users"
    test_dir.mkdir()
    monkeypatch.setattr(Users, "USERS_DIR", str(test_dir))
    return test_dir


def test_path1_old_user_missing_returns_false(isolated_users_dir):
    # Path condition: ¬E_old
    assert Users.update_user("ghost", "ghost2", "p") is False


def test_path2_rename_collision_returns_false(isolated_users_dir):
    # Path condition: E_old ∧ R ∧ E_new
    Users.create_user("alice", "p")
    Users.create_user("bob", "p")
    assert Users.update_user("alice", "bob", "p2") is False


def test_path3_update_ok_returns_true(isolated_users_dir):
    # Path condition: E_old ∧ (¬R ∨ ¬E_new)
    Users.create_user("alice", "p")
    assert Users.update_user("alice", "alice", "p2") is True
