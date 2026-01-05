import Menus


def test_popular_events_code_path_executes(monkeypatch, capsys):
    inputs = iter(["2", "7"])  # choose popular events then logout
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.user_menu("testuser")

    out = capsys.readouterr().out
    assert "Rock concert" in out
    assert "Christmas Party" in out
