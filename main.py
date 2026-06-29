# this is crossword solving, crossword generator is iin crossword,py

from testCrossword import puzzle


def main():
    cwPuzzle = {"down":{"test": "an exam"},
	"across":{"stay":"to remain"},
	"intersect":{"test":["stay",2,0]}}
    done = False
    while not done:
        printCrossword(cwPuzzle,-1,-1,-1)
        takeTurn(cwPuzzle)
        if checkCorrectDone(cwPuzzle):
            done=True
    return

def takeTurn(cw):
    cont = False
    while not cont:
        dir = input("pick a direction (Across/Down: ")
        if dir.lower() in ["a","across"]:
            dir = "across"
            cont = True
        if dir.lower() in ["d","down"]:
            dir="down"
            cont=True
    cont=False
    while not cont:
        try:
            num = int(input("which number would you like to fill in? "))
        except:
            num = -420
        if num>-1 and num<len(cw[dir].keys()):
            cont=True
        else:
            print("number out of range")
    cont = False
    while not cont:
        guess = input("make your guess: ")
        if len(guess) == len(cw[dir][num]):
            cw[dir][num].guess=guess
            if checkvalid(cw):
                cont=True
            else:
                cont=False
                print("invalid overlap")


def checkvalid(cw): # checks validity of guesses given overlaps in the puzzle.
    return True
            
                            
def checkCorrectDone(cw): #checks if puzzlr is finished and right
    return False

def placeCrossword(cw,hinum,hidir,solves):
    placementChart = {}
    for key,data in cw.down:
        print(key)




def printCrossword(crossword,hinum,hidirecction,solves):
     # create an array to hold the crossword
    # place wrds in array
    # trim empty rows and collumns
    # print array with no surrounding stuff
    X = "X"
    puzzleArray = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"]]
    for row in puzzleArray:
        for elem in row:
            print(elem,end="")
        print("")
    print(crossword)



main()
