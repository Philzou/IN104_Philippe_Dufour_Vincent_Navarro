import IN104_simulateur as simu
from evaluation import evaluate
from minimax_alphabeta import minimax_alphabeta
#simu.GameState.get_children = simu.GameState.findNextStates
#simu.GameState.evaluate = evaluate

class alphabeta_Brain:

	def __init__(self, config=None, rules=None,eval=evaluate):
		self.name = "AlphabetaBrain" # set your AI name here
		self.depth = 5 # Set the exploration depth here
		self.eval_function=eval
	def play(self, gameState, timeLimit):
		#use minimax here to return the next state with higher score
		s=0
		goodState= simu.GameState.findNextStates(gameState)[0]
		for state in simu.GameState.findNextStates(gameState):
			a=minimax_alphabeta(state,self.depth,True, simu.GameState.findNextStates, self.eval_function)
			if s<a:
				s=a
				goodState=state
		return goodState

	def __str__(self):
		return self.name
