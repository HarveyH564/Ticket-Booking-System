import Menus
import Events


def test_whitebox_date_range_calls_correct_function(monkeypatch):
    called = {"args": None}

    def fake(start, end):
        called["args"] = (start, end)
        return [{"name": "X", "date": "01-12-2025", "genre": "rock", "tickets_left": 1}]

    monkeypatch.setattr(Events, "filter_events_by_date_range", fake)

    inputs = iter(["1", "01-12-2025", "31-12-2025"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.filter_events_menu()
    assert called["args"] == ("01-12-2025", "31-12-2025")


def test_whitebox_tickets_left_calls_correct_function(monkeypatch):
    called = {"arg": None}

    def fake(min_left):
        called["arg"] = min_left
        return [{"name": "X", "date": "01-12-2025", "genre": "rock", "tickets_left": 1}]

    monkeypatch.setattr(Events, "filter_events_by_tickets_left", fake)

    inputs = iter(["2", "25"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.filter_events_menu()
    assert called["arg"] == "25"


def test_whitebox_genre_calls_correct_function(monkeypatch):
    called = {"arg": None}

    def fake(genre):
        called["arg"] = genre
        return [{"name": "X", "date": "01-12-2025", "genre": genre, "tickets_left": 1}]

    monkeypatch.setattr(Events, "filter_events_by_genre", fake)

    inputs = iter(["3", "jazz"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.filter_events_menu()
    assert called["arg"] == "jazz"
