import Menus
import Tickets


def test_view_previous_purchases_path(monkeypatch):
    called = {"hit": False}

    def fake_view_previous_purchases(username):
        called["hit"] = True

    monkeypatch.setattr(Tickets, "view_previous_purchases", fake_view_previous_purchases)

    inputs = iter(["5", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.user_menu("testuser")

    assert called["hit"] is True
