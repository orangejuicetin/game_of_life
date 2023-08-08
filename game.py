from enum import Enum
from typing import NoReturn
from time import sleep
import tkinter


class State(Enum):
    DEAD = 0
    ALIVE = 1


def initialize_gameboard() -> list[list[State]]:
    return [[State.DEAD] * 10 for _ in range(10)]


def assert_never(x: NoReturn) -> NoReturn:
    assert False, "Unhandled type: {}".format(type(x).__name__)


def get_alive_neighbor_count(gameboard: list[list[State]], x: int, y: int) -> int:
    neighbor_count = 0
    min_x = 0
    min_y = 0
    # Assume that gameboard is non-empty and every row is the same length
    max_x = len(gameboard[0])
    max_y = len(gameboard)
    for current_offset_x in range(-1, 2):
        for current_offset_y in range(-1, 2):
            if current_offset_y == 0 and current_offset_x == 0:
                continue
            # Need >= for maxs not just > because list indices are 0-indexed and the length
            # is therefore "too long" by one
            if current_offset_x + x >= max_x or current_offset_y + y >= max_y or current_offset_x + x < min_x or current_offset_y + y < min_y:
                continue
            cell_state = gameboard[x + current_offset_x][y + current_offset_y]
            match cell_state:
                case State.ALIVE:
                    neighbor_count += 1
                case State.DEAD:
                    pass
                case _:
                    assert_never(cell_state)
    return neighbor_count


def new_cell_state(gameboard: list[list[State]], x: int, y: int) -> State:
    num_of_alive_neighbors = get_alive_neighbor_count(
        gameboard=gameboard, x=x, y=y)
    current_cell_state: State = gameboard[x][y]
    if x == 1 and y == 1:
        print(f'{num_of_alive_neighbors=}')
    match current_cell_state:
        case State.ALIVE:
            if num_of_alive_neighbors < 2:
                return State.DEAD
            elif num_of_alive_neighbors == 2 or num_of_alive_neighbors == 3:
                return State.ALIVE
            else:
                return State.DEAD
        case State.DEAD:
            if num_of_alive_neighbors == 3:
                return State.ALIVE
            else:
                return State.DEAD


def play_one_round(gameboard: list[list[State]]) -> list[list[State]]:
    fresh_gameboard = initialize_gameboard()
    for x in range(len(gameboard[0])):
        for y in range(len(gameboard)):
            fresh_gameboard[x][y] = new_cell_state(gameboard, x, y)
    gameboard = fresh_gameboard


def update_canvas(gameboard: list[list[State]], root: tkinter.Tk) -> None:
    for row in range(len(gameboard[0])):
        for col in range(len(gameboard)):
            color = "black" if gameboard[row][col] == State.ALIVE else "white"
            square = tkinter.Label(root, bg=color, width=5, height=2)
            square.grid(row=col, column=row)


def upload_new_board_to_canvas(gameboard: list[list[State]], canvas: tkinter.Canvas) -> None:
    play_one_round(gameboard)
    update_canvas(gameboard, canvas)


def main():
    gameboard = initialize_gameboard()
    gameboard[1+4][0+4] = State.ALIVE
    gameboard[1+4][1+4] = State.ALIVE
    gameboard[1+4][2+4] = State.ALIVE
    gameboard[0+4][1+4] = State.ALIVE
    gameboard[2+4][0+4] = State.ALIVE
    window = tkinter.Tk()
    window.title("Game of Life")
    canvas = tkinter.Canvas(window, width=500, height=500)
    canvas.pack()
    update_canvas(gameboard, canvas)  # initialize the board
    next_button = tkinter.Button(
        window, text="Next Iteration", command=lambda: upload_new_board_to_canvas(gameboard, window))
    next_button.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
