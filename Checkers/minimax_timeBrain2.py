import IN104_simulateur as simu
from evaluation import evaluate
from minimax_time2 import minimax_alphabeta
from time import time
from evaluation2 import evaluate2
#simu.GameState.get_children = simu.GameState.findNextStates
#simu.GameState.evaluate = evaluate

class MinimaxBrain:

	def __init__(self, config=None , rules=None,eval=evaluate):
		self.name = "AII" # set your AI name here
		self.depth = 5 # Set the exploration depth here
		self.time_list = []
		self.eval_function=eval

	def play(self, gameState, timeLimit):
		#use minimax here to return the next state with higher score
		T=timeLimit
		t1=time()
		states=simu.GameState.findNextStates(gameState)
		N=len(states)
		goodState=states[0]
		m=-10**10
		t2=time()
		T=T-(t2-t1)
		for state in states:
			t3=time()
			s=minimax_alphabeta(state,T/N,True, simu.GameState.findNextStates, self.eval_function)
			N=N-1
			t4=time()
			T=T-(t4-t3)
			if m<s:
				m=s
				goodState=state
		self.time_list.append(time()-t1)
		return goodState

	def __str__(self):
		return self.name
