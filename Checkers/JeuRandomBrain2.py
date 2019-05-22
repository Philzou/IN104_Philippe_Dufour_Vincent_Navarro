#To launch a game between two (human) players with the default config:
import IN104_simulateur as simu

from RandomBrain import RandomBrain
from minimax_timeBrain2 import MinimaxBrain
from alphabeta_transpositionBrain import Minimax_alphabeta_transpositionBrain

from evaluation import evaluate
from evaluation2 import evaluate2

#brain1 = MinimaxBrain(eval=evaluate2)
#brain2 = MinimaxBrain(eval=evaluate)
brain1 = RandomBrain()
brain2 = MinimaxBrain(eval=evaluate)
timeLimit = 0.1 # each player will have 10 seconds to play
game = simu.Game(brain1, timeLimit, brain2, timeLimit, rules = {'noCaptureMax' : 25})
game.displayLevel=1
game.runGame()
print(game.pdn) # display the game summary

fichier=open("fichier.txt","w")
fichier.write(game.pdn)
fichier.close()

L1 = brain1.time_list
L2 = brain2.time_list
print(max(L1))
print(min(L1))
print(sum(L1)/len(L1))
print(max(L2))
print(min(L2))
print(sum(L2)/len(L2))
