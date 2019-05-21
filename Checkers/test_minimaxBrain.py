import IN104_simulateur as simu
from MinimaxBrain import MinimaxBrain
from RandomBrain import RandomBrain
brain1 = RandomBrain()
human_time = 15 #the human will have 10 secs to play
brain2 = MinimaxBrain()
ai_time = 1 #the AI will only have 1 sec to play
game = simu.Game(brain1, human_time, brain2, ai_time)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game. 
