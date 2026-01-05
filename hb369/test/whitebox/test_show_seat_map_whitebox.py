from Menus import show_seat_map


def test_show_seat_map_executes_and_prints_header(capsys):
    show_seat_map()
    out = capsys.readouterr().out
    assert "Seat Map" in out
