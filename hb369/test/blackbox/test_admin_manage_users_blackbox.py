import Menus
import Users


def _set_inputs(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(it))


def test_admin_view_users_no_users(monkeypatch, capsys):
    # choice 1 -> list users returns empty -> prints "No users found!" -> choice 5 exits
    monkeypatch.setattr(Users, "list_all_users", lambda: [])
    _set_inputs(monkeypatch, ["1", "5"])

    Menus.admin_manage_user_menu()
    out = capsys.readouterr().out

    assert "ADMIN MANAGE USER" in out
    assert "No users found!" in out


def test_admin_view_users_some_users(monkeypatch, capsys):
    monkeypatch.setattr(Users, "list_all_users", lambda: ["alice", "bob"])
    _set_inputs(monkeypatch, ["1", "5"])

    Menus.admin_manage_user_menu()
    out = capsys.readouterr().out

    assert "User:" in out
    assert "alice" in out
    assert "bob" in out


def test_admin_add_user_success(monkeypatch, capsys):
    monkeypatch.setattr(Users, "create_user", lambda u, p: True)
    _set_inputs(monkeypatch, ["2", "newuser", "pass123", "5"])

    Menus.admin_manage_user_menu()
    out = capsys.readouterr().out

    assert "User created successfully!" in out


def test_admin_add_user_duplicate(monkeypatch, capsys):
    monkeypatch.setattr(Users, "create_user", lambda u, p: False)
    _set_inputs(monkeypatch, ["2", "takenname", "pass123", "5"])

    Menus.admin_manage_user_menu()
    out = capsys.readouterr().out

    assert "username already taken!" in out


def test_admin_update_user_user_does_not_exist(monkeypatch, capsys):
    monkeypatch.setattr(Users, "user_exists", lambda u: False)
    _set_inputs(monkeypatch, ["3", "ghost", "5"])

    Menus.admin_manage_user_menu()
    out = capsys.readouterr().out

    assert "User does not exist!" in out


def test_admin_delete_user_success(monkeypatch, capsys):
    monkeypatch.setattr(Users, "delete_user", lambda u: True)
    _set_inputs(monkeypatch, ["4", "alice", "5"])

    Menus.admin_manage_user_menu()
    out = capsys.readouterr().out

    assert "User deleted." in out


def test_admin_delete_user_not_found(monkeypatch, capsys):
    monkeypatch.setattr(Users, "delete_user", lambda u: False)
    _set_inputs(monkeypatch, ["4", "ghost", "5"])

    Menus.admin_manage_user_menu()
    out = capsys.readouterr().out

    assert "User not found." in out


def test_admin_invalid_menu_option(monkeypatch, capsys):
    _set_inputs(monkeypatch, ["99", "5"])
    Menus.admin_manage_user_menu()
    out = capsys.readouterr().out

    assert "Invalid option." in out
