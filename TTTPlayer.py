import random
from rules import *


class TTTPlayer:

    def __init__(self, playerType):
        if playerType in [0,1,2,3]:
            self.playerType = playerType
            self.ttt_board = [0]*9
        else:
            print("Unsupported player type provided:", playerType)
            quit()

    def makeMove(self): #, ttt_board_in):
        if self.playerType == 0:
            #return self.makeRandomMove(ttt_board_in)
            return self.makeRandomMove()
        elif self.playerType == 1:
            #return self.makeRulesMove(ttt_board_in)
            return self.makeRulesMove()
        elif self.playerType == 3:
            move = int(input("Enter move: "))
            return move
        else:
            print("Need AI")

    #Make random move
    def makeRandomMove(self): #,boardIn):
        # Find empty spots on board
        #print("Making random move")
        #zero_indexes = [i for i in range(len(boardIn)) if boardIn[i] == 0]

        zero_indexes = [i for i in range(len(self.ttt_board)) if self.ttt_board[i] == 0]
        myMove = random.choice(zero_indexes)
        return myMove

    #Make rules-based move
    def makeRulesMove(self): #,boardIn):
        #check to see if you can win, or if the opponenet will win next move
        rows_of_three = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

        #the way that this is set up, combo has to be 0 -1 1 or something like that
        for combo in rows_of_three:
            if immediate(self, combo, 1) != -1:
                #nothing has changed since the last time we called it
                toMove = immediate(self, combo, 1)
                return toMove
            elif immediate(self, combo, -1) != -1:
                toMove = immediate(self, combo, -1)
                return toMove

        #check to see if you can make a move that is connected to another one of your moves next to an open space
        #if not, block your opponent from making a move
        for combo in rows_of_three:
            if next_to(self, combo, 1) != -1:
                toMove = next_to(self, combo, 1)
                return toMove
            elif next_to(self, combo, -1) != -1:
                toMove = next_to(self, combo, -1)
                return toMove


        #check to see if you can make a move that is connected to one of your previous moves
        

        #if everything else fails, check if the middle of the board has been taken
        zero_indexes = [i for i in range(len(self.ttt_board)) if self.ttt_board[i] == 0]
        corners = [0, 2, 6, 8]

        if 4 in zero_indexes:
            #print("first move")
            return 4



        return random.choice(zero_indexes)
