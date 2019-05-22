import sys
from time import time
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
        self.time_list=[]
		
    def play(self, gameState, timeLimit):
        t1=time()
        possibleMoves = gameState.findPossibleMoves()
        print(gameState.toDisplay(True))
        
        
        while True:
            try:
                a=random.randint(0,len(possibleMoves)-1)
                move= possibleMoves[a]
                choice = gameState.doMove(move, inplace = False)
                break
            except TimeOutException as e:
                print('Sorry, you took too much time to think !')
                raise e
        self.time_list.append(time()-t1)
        return choice


    def __str__(self):
        return self.name
