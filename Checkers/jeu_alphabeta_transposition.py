#To launch a game between two (human) players with the default config:
import IN104_simulateur as simu
from RandomBrain import RandomBrain
from alphabeta_transpositionBrain import MinimaxBrain

brain1 = RandomBrain()
brain2 = MinimaxBrain()
timeLimit = 100 # each player will have 10 seconds to play
game = simu.Game(brain1, timeLimit, brain2, timeLimit)
game.runGame()
print(game.pdn) # display the game summary

fichier=open("fichier.txt","w")
fichier.write(game.pdn)
fichier.close()
