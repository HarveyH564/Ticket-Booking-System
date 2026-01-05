import Tickets
import Events

def test_sold_out_branch_sets_tickets_left_to_zero(monkeypatch, capsys, tmp_path):
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

    Tickets.purchase_ticket("testuser", "1", "1", 1)

    out = capsys.readouterr().out
    assert Events.EVENTS["1"]["tickets_left"] == 0
    assert "This event is now SOLD OUT." in out
