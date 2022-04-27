from grid import Cell


def test_letter_initializes_as_undetermined():
    letter = Cell()
    assert letter.get_state() == Cell.UNDETERMINED