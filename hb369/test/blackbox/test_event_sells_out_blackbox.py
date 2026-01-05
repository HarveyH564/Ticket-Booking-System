import Tickets
import Events

def test_event_prints_sold_out_when_last_ticket_bought(monkeypatch, capsys, tmp_path):
    monkeypatch.chdir(tmp_path)

    monkeypatch.setattr(Events, "EVENTS", {
        "1": {
            "name": "Last Ticket Event",
            "date": "10-12-2025",
            "tickets_left": 1,
            "prices": {"general": 10, "vip": 20, "meet_greet": 30}
        }
    })

    inputs = iter(["Y", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = Tickets.purchase_ticket("testuser", "1", "1", 1)

    out = capsys.readouterr().out
    assert result is True
    assert "This event is now SOLD OUT." in out
