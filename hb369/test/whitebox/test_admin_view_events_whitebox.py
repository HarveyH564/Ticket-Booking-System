import Menus
import Events

def test_admin_view_events_calls_events_function(monkeypatch):
    called = {"hit": False}

    def fake_show_available_events():
        called["hit"] = True

    monkeypatch.setattr(Events, "show_available_events", fake_show_available_events)

    inputs = iter(["2", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.admin_menu()

    assert called["hit"] is True
