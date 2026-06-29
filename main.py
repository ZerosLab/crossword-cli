# this is crossword solving, crossword generator is iin crossword,py

from testCrossword import puzzle
#from crossword import generateCrossword

def main():
    cwPuzzle = {"down":[["test", "an exam",False]],
	        "across":[["stay","to remain",False]],
	"intersect":{"test":["stay",2,0]}}
    #cwPuzzle = generateCrossword()
    done = False
    while not done:
        printCrossword(cwPuzzle,-1,-1,-1)
        takeTurn(cwPuzzle)
        if checkCorrectDone(cwPuzzle):
            done=True
    print("CONGRATS!!! You win!")
    return

def takeTurn(cw):
    cont = False
    while not cont:
        dir = input("pick a direction (Across/Down): ")
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
        if num>-1 and num<len(cw[dir]):
            cont=True
        else:
            print("number out of range")
    cont = False
    while not cont:
        guess = input("make your guess: ")
        if len(guess) == len(cw[dir][num][0]):
            cw[dir][num][2]=guess
            if checkvalid(cw):
                cont=True
            else:
                cont=False
                print("invalid overlap")
            


def checkvalid(cw): # checks validity of guesses given overlaps in the puzzle.
    for word in cw["down"]:
        if word[0] in cw["intersect"].keys():
            crossWord = cw["intersect"][word[0]][0]
            for palabra in cw["across"]:
                if palabra[2] and word[2]:
                    try:
                        if palabra[2][cw["intersect"][word[2]][2]] != word[2][cw["intersect"][word[2]][1]]:
                            #print(palabra[2][cw["intersect"][word[2]][2]])
                            #print(word[2][cw["intersect"][word[2]][1]])
                            return False
                    except:
                        print("error")
    return True
            
                            
def checkCorrectDone(cw): #checks if puzzlr is finished and right
    for word in cw["across"]:
        if word[0]!=word[2]:
            return False
    for word in cw["down"]:
        if word[0]!=word[2]:
            return False
    return True

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
    placements = {}
    maxDwn = 1
    for word in crossword["down"]:
        maxDwn += len(word)
    maxAcc = 1
    for word in crossword["across"]:
        maxAcc+=len(word)
    puzzleArray = [["X"]*maxAcc]*maxDwn
    #place first down at 0,0
    placements[crossword["down"][0][0]]=(0,0,0)
        
    # figure first intersection, place and shift if necessary
    # loop 
    for row in puzzleArray:
        for elem in row:
            print(elem,end="")
        print("")
    print(crossword)

def moveR(cw):
    for word in cw.keys():
        cw[word][0]+=1

def moveL(cw):
    for word in cw.keys():
        cw[word][0]-=1
def moveD(cw):
    for word in cw.keys():
        cw[word][1]+=1
def moveU(cw):
    for word in cw.keys():
        cw[word][1]-=1

main()
