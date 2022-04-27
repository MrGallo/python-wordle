from grid import WordGrid, Row, Cell


def test_wordgrid_initializes_with_six_rows_of_letters():
    grid = WordGrid()
    assert len(grid.get_rows()) == 6
    for row in grid.get_rows():
        assert type(row) is Row

        assert len(row.get_cells()) == 5
        for letter in row.get_cells():
            assert type(letter) is Cell


def test_grid_add_letter():
    grid = WordGrid()
    grid.add_letter("h")
    assert grid.get_rows()[0].get_word() == "h"
    for row in grid.get_rows()[1:]:
        assert row.get_word() == ""

def test_grid_add_multiple_words():
    grid = WordGrid()

    for c in "hello":
        grid.add_letter(c)
    
    assert grid.get_rows()[0].get_word() == "hello"

    grid.submit_word()  # what happens here?