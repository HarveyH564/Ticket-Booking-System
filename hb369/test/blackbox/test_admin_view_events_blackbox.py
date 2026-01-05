import Menus
import Events

def test_admin_view_events_shows_output(monkeypatch, capsys):
    def fake_show_available_events():
        print("EVENT LIST")
        print("1. Test Event")

    monkeypatch.setattr(Events, "show_available_events", fake_show_available_events)

    inputs = iter(["2", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.admin_menu()

    out = capsys.readouterr().out
    assert "EVENT LIST" in out
    assert "Test Event" in out
