import Menus
import Users


def _set_inputs(monkeypatch, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(it))


def test_whitebox_choice_1_calls_list_all_users(monkeypatch):
    called = {"count": 0}

    def fake_list_all_users():
        called["count"] += 1
        return []

    monkeypatch.setattr(Users, "list_all_users", fake_list_all_users)
    _set_inputs(monkeypatch, ["1", "5"])

    Menus.admin_manage_user_menu()

    assert called["count"] == 1


def test_whitebox_choice_2_calls_create_user(monkeypatch):
    called = {"args": None}

    def fake_create_user(u, p):
        called["args"] = (u, p)
        return True

    monkeypatch.setattr(Users, "create_user", fake_create_user)
    _set_inputs(monkeypatch, ["2", "u1", "p1", "5"])

    Menus.admin_manage_user_menu()

    assert called["args"] == ("u1", "p1")


def test_whitebox_choice_4_calls_delete_user(monkeypatch):
    called = {"arg": None}

    def fake_delete_user(u):
        called["arg"] = u
        return True

    monkeypatch.setattr(Users, "delete_user", fake_delete_user)
    _set_inputs(monkeypatch, ["4", "u_to_delete", "5"])

    Menus.admin_manage_user_menu()

    assert called["arg"] == "u_to_delete"
