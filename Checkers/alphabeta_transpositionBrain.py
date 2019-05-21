import IN104_simulateur as simu
from evaluation import evaluate
from minimax_alphabeta_transposition import minimax
simu.GameState.get_children = simu.GameState.findNextStates
simu.GameState.evaluate = evaluate

class MinimaxBrain:

	def __init__(self, config=None, rules=None):
		self.name = "AIII" # set your AI name here
		self.depth = 5 # Set the exploration depth here

	def play(self, gameState, timeLimit):
		#use minimax here to return the next state with higher score
		s=0
		goodState=gameState.findNextStates()[0]
		for state in gameState.findNextStates():
			if s<minimax(state,self.depth,True):
				s=minimax(state,self.depth,True)
				goodState=state
		return goodState

	def __str__(self):
		return self.name
