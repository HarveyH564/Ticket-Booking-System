import Menus


def test_popular_upcoming_events_printed(monkeypatch, capsys):
    inputs = iter(["2", "7"])  # option 2 = popular events, 7 = logout

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.user_menu("testuser")

    out = capsys.readouterr().out

    assert "Popular Upcoming Events" in out
    assert "Rock concert" in out
    assert "Christmas Party" in out
