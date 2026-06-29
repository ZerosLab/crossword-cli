import defslist as d

def generateCrossword():
    print("Select desired crossword puzzle difficulty (enter number between 1 and 10)")
    
    while not (diff) :
        diff = (input("> "))
        try:
            diff = int(diff)
        except:
            diff = False
    numWordsVert = int(diff*2)
    numWordsHoriz = diff*2
    
    i=0
    while i<numWordsVert:
        i+=1
    # todo randomly select vverticla words with no repeats
    # todo loop and randomly select horiz words w no repeats
    # todo find shared letters and determine placement
