import IN104_simulateur as simu
from evaluation import evaluate
from minimax import minimax
from time import time
simu.GameState.get_children = simu.GameState.findNextStates
simu.GameState.evaluate = evaluate

class MinimaxBrain:

	def __init__(self, config=None, rules=None):
		self.name = "AIII" # set your AI name here
		self.depth = 5 # Set the exploration depth here
		

	def play(self, gameState, timeLimit):
		#use minimax here to return the next state with higher score
		s=0
		T=timeLimit
		t1=time()
		states=gameState.findNextStates()
		goodState=states[0]
		t2=time()
		for state in states:
			if s<minimax(state,T-(t2-t1),True):
				s=minimax(state,T-(t2-t1),True)
				goodState=state
		return goodState

	def __str__(self):
		return self.name
