# This is what w3schools told me to do (I didn't want to use the gemini AI result that came up instantly with a google search)
# https://www.w3schools.com/python/numpy/numpy_getting_started.asp

# I'm using numpy for 2d arrays! which is how I would make this if I was using Java
import numpy as np

# Enums!! (might be excessive but whatever it makes sense to me)
# https://www.geeksforgeeks.org/python/enum-in-python/
from enum import Enum, auto

class Room(Enum):
    START = auto()
    HALLWAY = auto()
    RIDDLE = auto()
    PUZZLE = auto() # undertale inspired fr
    END = auto()

maze = np.array([
    [None        , None        , None        , None        , None        , None        , None        ],
    [None        , Room.RIDDLE , None        , Room.END    , Room.HALLWAY, None        , None        ],
    [None        , Room.HALLWAY, Room.HALLWAY, Room.HALLWAY, Room.HALLWAY, Room.PUZZLE , None        ],
    [None        , None        , None        , Room.HALLWAY, None        , Room.HALLWAY, None        ],
    [None        , Room.HALLWAY, Room.HALLWAY, Room.PUZZLE , Room.HALLWAY, Room.HALLWAY, None        ],
    [None        , Room.PUZZLE , None        , Room.HALLWAY, None        , Room.RIDDLE , None        ],
    [None        , None        , Room.HALLWAY, Room.HALLWAY, Room.PUZZLE , None        , None        ],
    [None        , None        , None        , Room.START  , None        , None        , None        ],
])

pIndex = np.where(maze == Room.START)
row, col = pIndex[0][0], pIndex[1][0]

puzzleKeys = 0
puzzleKeysNeeded = 4

riddleKeys = 0
riddleKeysNeeded = 2

circuit_link = ""

game_running = True

def IsInBounds(row, col):
    return row >= 0 and row < maze.shape[0] and col >= 0 and col < maze.shape[1]

def IsIndexRoom(row, col, room):
    return IsInBounds(row, col) and maze[row, col] == room

def PrintMaze():
    for (r, c), x in np.ndenumerate(maze):
        #◆▲■◌●◈◎◯
        icon = ""
        if(IsIndexRoom(r, c, Room.HALLWAY)):
            icon = "•"
        elif(IsIndexRoom(r, c, Room.START)):
            icon = "S"
        elif(IsIndexRoom(r, c, Room.END)):
            icon = "E"
        elif(IsIndexRoom(r, c, Room.PUZZLE)):
            icon = "◈"
        elif(IsIndexRoom(r, c, Room.RIDDLE)):
            icon = "◎"
        else:
            icon = "▢"

        if((r, c) == (row, col)):
            icon = "◆"
        
        print(f" {str(icon)} ", end="")

        if(c == maze.shape[1]-1):
            print("")

def PuzzleRoom(row, col):
    beatRoom = False
    global puzzleKeys
    print(f"\n[PUZZLE ROOM]\n")
    while not beatRoom:
        if puzzleKeys == 0:
            try:
                if int(input(f"What is 2+2?\n")) == 4:
                    print(f"Correct.\n")
                    beatRoom = True
                    puzzleKeys+=1
                    return
                else:
                    print("WRONG ANSWER.")
            except ValueError:
                print("INPUT A NUMBER!!")
        elif puzzleKeys == 1:
            print(f"How straight (ambiguous meaning) are you?\n1. As straight as the curvature of the sun\n2. Like a ruler\n3. Like a bent ruler\n")
            try:
                answer = int(input(f"Enter your answer:\n"))
                print(f"There's no wrong answer! {answer}/{answer} amazing points.")
                puzzleKeys+=1
                beatRoom = True
                return
            except ValueError:
                print("INPUT A NUMBER!!")
        elif puzzleKeys == 2:
            print(f"Go to the following link (it just goes to the image in this repo - its very similar to a question on the physics 2 test i FAILED 😣) and solve for E2/EMF (έ2 - this was the only epsilon symbol I could find) in μV, plus the ΣΩ of the resistors who's current is <5A, divided by the τ of a 5 μF capacitor assuming it replaced the R4:\n")
            try:
                answer = int(input(f"Enter your answer:\n"))
                print(f"I actually didn't want to solve this myself because I was too lazy, and I wanted to throw you off by adding a bunch of symbols and concepts, so yeah, free point.")
                puzzleKeys+=1
                beatRoom = True
                return
            except ValueError:
                print("INPUT A NUMBER!!")
        elif puzzleKeys == 3:
            print(f"Pick up the key you see in front of you? (Y/N)\n")
            answer = input(f"Enter your answer:\n")[0].upper()
            if answer == "Y":
                print("Okay.")
                puzzleKeys+=1
                beatRoom = True
                return
            elif answer == "N":
                print(f"Why\n")
            else:
                print("Invalid Answer...")


def RiddleRoom(row, col):
    beatRoom = False
    global riddleKeys
    print(f"\n[RIDDLE ROOM]\n")
    while not beatRoom:
        if riddleKeys == 0:
            print("Star Wars TCW reference: You can run but cannot walk; You have a mouth but cannot talk; You have a head but never weep; You have a bed but never sleep.")
            answer = input(f"You are a(n) _____.\n").lower()
            if answer == "river":
                print("Correct!")
                riddleKeys+=1
                beatRoom = True
                return
            else:
                print("Try again!")
        if riddleKeys == 1:
            print(f"What has to be broken before you can use it?\n")
            answer = input(f"A(n) _____.\n").lower()
            if answer == "egg":
                print("Correct!")
                riddleKeys+=1
                beatRoom = True
                return
            else:
                print("Try again!")


while game_running:
    print(f"{row} {col}")
    if IsIndexRoom(row, col, Room.END) and puzzleKeys == puzzleKeysNeeded and riddleKeys == riddleKeysNeeded:
        print("\nYOU BEAT THE GAME!")
        game_running = False
        break
    elif(IsIndexRoom(row, col, Room.PUZZLE)):
        PuzzleRoom(row, col)
        maze[row, col] = Room.HALLWAY
    elif(IsIndexRoom(row, col, Room.RIDDLE)):
        RiddleRoom(row, col)
        maze[row, col] = Room.HALLWAY

    print(f"\nYou: ◆\nPuzzle: ◈\nRiddle: ◎")
    PrintMaze()

    print(f"You have {puzzleKeys + riddleKeys}/{riddleKeysNeeded + puzzleKeysNeeded} keys to win!")

    move = str(input("Move with WASD:\n"))[0].lower()

    tempRow = row
    tempCol = col

    match move:
        case "w":
            tempRow = tempRow - 1
        case "a":
            tempCol = tempCol - 1
        case "s":
            tempRow = tempRow + 1
        case "d":
            tempCol = tempCol + 1
        case _:
            print("Invalid input!")
            continue
    
    if IsInBounds(tempRow, tempCol) and not IsIndexRoom(tempRow, tempCol, None):
        row = tempRow
        col = tempCol