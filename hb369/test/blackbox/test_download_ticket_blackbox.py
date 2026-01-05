import Tickets
import Events

def test_download_message_after_purchase(monkeypatch, capsys, tmp_path):
    monkeypatch.chdir(tmp_path)

    monkeypatch.setattr(Events, "EVENTS", {
        "1": {
            "name": "Test Event",
            "date": "01-12-2025",
            "tickets_left": 10,
            "prices": {"general": 20, "vip": 50, "meet_greet": 100}
        }
    })

    inputs = iter(["Y", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    Tickets.purchase_ticket("testuser", "1", "1", 1)

    out = capsys.readouterr().out
    assert "Ticket successfully downloaded!" in out
