import sys
import time
from IN104_simulateur.gameState import GameState
from IN104_simulateur.move import Move
from IN104_simulateur.player import TimeOutException
import random

class RandomBrain:
    numero=1
    def __init__(self):
        self.name ='joueur'+str(RandomBrain.numero)
        RandomBrain.numero+=1
        self.alwaysSeeAsWhite = False

    def play(self, gameState, timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        print(gameState.toDisplay(True))
        
        
        while True:
            try:
                a=random.randint(0,len(possibleMoves)-1)
                move= possibleMoves[a]
                choice = gameState.doMove(move, inplace = False)
                break
            except TimeOutException as e:
                print('Sorry, you took to much time to think !')
                raise e
        return choice


    def __str__(self):
        return self.name
