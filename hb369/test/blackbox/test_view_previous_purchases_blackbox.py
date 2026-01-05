import Menus
import Tickets


def test_view_previous_purchases_called(monkeypatch, capsys):
    called = {"username": None}

    def fake_view_previous_purchases(username):
        called["username"] = username
        print("Previous purchases:")
        print("Event A - Ticket 1")

    monkeypatch.setattr(Tickets, "view_previous_purchases", fake_view_previous_purchases)

    inputs = iter(["5", "7"])  # view purchases, then logout
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.user_menu("testuser")

    out = capsys.readouterr().out

    assert called["username"] == "testuser"
    assert "Previous purchases" in out
    assert "Event A" in out
