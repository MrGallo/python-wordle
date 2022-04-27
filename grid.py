from typing import List, Optional


class Cell:
    CORRECT_POSITION = 0
    IN_WORD = 1
    NOT_IN_WORD = 2
    UNDETERMINED = 3

    def __init__(self):
        self._letter: Optional[str] = None
        self._state = Cell.UNDETERMINED

    def get_state(self):
        return self._state
    
    def set_letter(self, letter: str):
        self._letter = letter
    
    def clear(self):
        self._letter = None
    
    def get_letter(self) -> str:
        if self._letter is None:
            return ""

        return self._letter


class RowFullError(Exception):
    pass


class RowEmptyError(Exception):
    pass


class Row:
    def __init__(self):
        self._letters: List[Cell] = []
        for _ in range(5):
            self._letters.append(Cell())
        
        self._current_letter_index = 0

    def get_cells(self) -> List[Cell]:
        return self._letters

    def get_word(self) -> str:
        word = ""
        for cell in self._letters:
            word += cell.get_letter()

        return word

    def add_letter(self, letter: str) -> None:
        if len(letter) != 1:
            raise ValueError("Can only add one letter at a time.")

        if self._current_letter_index == len(self._letters):
            raise RowFullError

        self._letters[self._current_letter_index].set_letter(letter)
        self._current_letter_index += 1

    def remove_last(self) -> None:
        if self._current_letter_index - 1 < 0:
            raise RowEmptyError("There is no letter to remove.")

        self._letters[self._current_letter_index - 1].clear()
        self._current_letter_index -= 1

class Grid:
    def __init__(self):
        self._rows: List[Row] = []


class WordGrid(Grid):
    def __init__(self):
        super().__init__()
        for _ in range(6):
            self._rows.append(Row())
        
        self._current_row_index = 0
    
    def get_rows(self):
        return self._rows

    def add_letter(self, letter: str) -> None:
        row = self._rows[self._current_row_index]
        row.add_letter(letter)

class Keyboard(Grid):
    pass
