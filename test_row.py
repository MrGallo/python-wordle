import pytest

from grid import Row, RowFullError, RowEmptyError


def test_row_add_letter():
    row = Row()
    assert row.get_word() == ""

    row.add_letter("h")
    assert row._letters[0]._letter == "h"

    row.add_letter("e")
    assert row._letters[1]._letter == "e"
   

def test_rows_do_not_exceed_5_characters():
    row = Row()
    for n in range(5):
        row.add_letter("x")
    
    with pytest.raises(RowFullError):
        row.add_letter("a")


def test_add_letter_accepts_only_one_character():
    row = Row()

    with pytest.raises(ValueError):
        row.add_letter("ha")

    with pytest.raises(ValueError):
        row.add_letter("")


def test_row_get_word():
    row = Row()
    assert len(row.get_cells()) == 5
    
    row.add_letter("h")
    assert row.get_word() == "h"

    row.add_letter("e")
    row.add_letter("l")
    row.add_letter("l")
    row.add_letter("o")
    assert row.get_word() == "hello"


def test_remove_letter_from_row():
    row = Row()
    for n in range(5):
        row.add_letter(str(n))

    assert row.get_word() == "01234"

    row.remove_last()
    assert row.get_word() == "0123"


def test_remove_letter_from_empty_row_raises_row_empty_error():
    row = Row()
    with pytest.raises(RowEmptyError):
        row.remove_last()

