from enum import Enum

class State(Enum):
    DEAD = 0
    ALIVE = 1

def check_neighbors(gameboard, x, y):
    neighbor_count = 0
    if gameboard[x][y-1]:
    if gameboard[x][y+1]:
    if gameboard[x-1][y]:
    if gameboard[x-1][y-1]:
    if gameboard[x-1][y+1]:
    if gameboard[x+1][y]:
    if gameboard[x+1][y+1]:
    if gameboard[x+1][y-1]:
        
    
def main():
    gameboard = [[State.DEAD] * 25 for _ in range(25)]
    while True:
        for x in range(25):
            for y in range(25): 
                if not gameboard[x][y]:
                    
                    
      
    
main()
