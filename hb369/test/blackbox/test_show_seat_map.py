from Menus import show_seat_map


def test_show_seat_map_prints_layout(capsys):
    show_seat_map()
    out = capsys.readouterr().out

    # Basic checks
    assert "Seat Map" in out
    assert "1  2  3  4  5" in out

    # Row labels
    for row in ["A |", "B |", "C |", "D |", "E |"]:
        assert row in out

    # Seat symbols
    assert "O" in out
    assert "X" in out
