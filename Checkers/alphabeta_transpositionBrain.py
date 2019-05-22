import IN104_simulateur as simu
from evaluation import evaluate
from minimax_alphabeta_transposition import minimax
#simu.GameState.get_children = simu.GameState.findNextStates
#simu.GameState.evaluate = evaluate

class MinimaxBrain:

	def __init__(self, config=None, rules=None,eval=evaluate):
		self.name = "alphabeta_transpositionBrain" # set your AI name here
		self.depth = 5 # Set the exploration depth here
		self.eval_function=eval
	def play(self, gameState, timeLimit):
		#use minimax here to return the next state with higher score
		s=0
		goodState=simu.GameState.findNextStates(gameState)[0]
		for state in simu.GameState.findNextStates(gameState):
			a=minimax(state,self.depth,True,simu.GameState.findNextStates, self.eval_function)
			if s<a:
				s=a
				goodState=state
		return goodState

	def __str__(self):
		return self.name
