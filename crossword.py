import defslist as d

print("Select desired crossword puzzle difficulty (enter number between 1 and 10)")
diff = int(input("> "))

emptySquare="[_]"
nullSquare="[ ]"

numWordsVert = int(diff*1.75)
numWordsHoriz = diff*2

i=0
while i<numWordsVert:
    i+=1
    # todo randomly select vverticla words with no repeats

# todo loop and randomly select horiz words w no repeats

# todo find shared letters and determine placement 

# todo arrange letters in array

# todo print array as a crossword 

# todo print clues and numbers 

# todo allow interaction - selecting clue number and entring answer

# todo show filled answers on screen 

# todo verify correctness of answers