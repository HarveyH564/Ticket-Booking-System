import Menus
import Events


def test_filter_by_date_range_prints_results(monkeypatch, capsys):
    monkeypatch.setattr(
        Events,
        "filter_events_by_date_range",
        lambda start, end: [{"name": "Test Event", "date": "10-12-2025", "genre": "rock", "tickets_left": 5}],
    )

    inputs = iter(["1", "01-12-2025", "31-12-2025"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.filter_events_menu()

    out = capsys.readouterr().out
    assert "FILTER RESULTS" in out
    assert "Test Event" in out
    assert "10-12-2025" in out
    assert "rock" in out
    assert "Tickets left: 5" in out


def test_filter_by_tickets_left_prints_results(monkeypatch, capsys):
    monkeypatch.setattr(
        Events,
        "filter_events_by_tickets_left",
        lambda min_left: [{"name": "Big Event", "date": "15-12-2025", "genre": "pop", "tickets_left": 100}],
    )

    inputs = iter(["2", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.filter_events_menu()

    out = capsys.readouterr().out
    assert "FILTER RESULTS" in out
    assert "Big Event" in out
    assert "Tickets left: 100" in out


def test_filter_by_genre_prints_results(monkeypatch, capsys):
    monkeypatch.setattr(
        Events,
        "filter_events_by_genre",
        lambda genre: [{"name": "Jazz Night", "date": "20-12-2025", "genre": "jazz", "tickets_left": 12}],
    )

    inputs = iter(["3", "jazz"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.filter_events_menu()

    out = capsys.readouterr().out
    assert "FILTER RESULTS" in out
    assert "Jazz Night" in out
    assert "Genre: jazz" in out


def test_filter_no_results_prints_no_match(monkeypatch, capsys):
    monkeypatch.setattr(Events, "filter_events_by_genre", lambda genre: [])

    inputs = iter(["3", "metal"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Menus.filter_events_menu()

    out = capsys.readouterr().out
    assert "No events matched your filter." in out
