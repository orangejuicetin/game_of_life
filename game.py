from enum import Enum
from typing import NoReturn


class State(Enum):
    DEAD = 0
    ALIVE = 1


def initialize_gameboard() -> list[list[State]]:
    return [[State.DEAD] * 25 for _ in range(25)]


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
            if current_offset_x + x >= max_x or current_offset_y + y >= max_y or current_offset_x + x < min_x or current_offset_y < min_y:
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
    num_of_alive_neighbors = get_alive_neighbor_count(gameboard=gameboard, x=x, y=y)
    current_cell_state: State = gameboard[x][y]
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
    return fresh_gameboard


def main():
    gameboard = [[State.DEAD] * 5 for _ in range(5)]
    gameboard[3][3] = State.ALIVE
    gameboard[2][3] = State.ALIVE
    gameboard[2][2] = State.ALIVE
    print(play_one_round(gameboard))


if __name__ == "__main__":
    main()
