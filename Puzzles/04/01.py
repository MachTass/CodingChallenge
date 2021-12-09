class bingoBoard:
    def __init__(self, row1, row2, row3, row4, row5):
        self.board = []
        tempboard = [row1.split(), row2.split(),row3.split(),row4.split(), row5.split()]

        for boardidx, boardval in enumerate(tempboard):
            temparray = []
            for rowidx, rowval in enumerate(boardval):
                temparray.append(bingoSquare(rowval))
            self.board.append(temparray)

    def calculateVictoryBoard(self):
        unmarkedSum = 0
        for r in self.board:
            for v in r:
                if not v.marked:
                    unmarkedSum += int(v.value)
        print(f"final value = {unmarkedSum * int(self.recentValue)}")
        quit()

    def numberCalled(self, value):
        self.recentValue = value
        for r in self.board:
            for n in r:
                n.tryMark(value)

    def checkForWinCondition(self):
        #check rows
        for r in self.board:
            if (sum(x.marked for x in r) == 5):
                self.calculateVictoryBoard()
        for c in range(0, len(self.board)):
            markedAmount = 0
            for d in range(0, len(self.board[c])):
                if self.board[d][c].marked:
                    markedAmount += 1
            if markedAmount == 5:
                self.calculateVictoryBoard()

class bingoSquare:
    def __init__(self, value):
        self.value = value
        self.marked = False

    def tryMark(self, value):
        if self.value == value:
            self.marked = True

gameValues = None
gameBoards = []

with open('bingo-boards-test.txt') as f:
    gameValues = f.readline().rstrip().split(",")
    while (f.readline()):
        oneboard = bingoBoard(f.readline(), f.readline(), f.readline(), f.readline(), f.readline())
        gameBoards.append(oneboard)
    print(len(gameBoards))
    #play the game
    for number in gameValues:
        print (f"Calling number:{number}")
        for board in gameBoards:
            board.numberCalled(number)
            board.checkForWinCondition()
    print ("No boards won??")