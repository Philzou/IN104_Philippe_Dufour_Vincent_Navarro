from time import time

def minimax_alphabeta(state, T,maximize, alpha=-10**10, beta=10**10):
# calculer le score ici à l’aide de state.get_children() et state.evaluate()
	t1=time()
	temps=3E-4
	states=state.get_children()
	if T<temps or len(state.get_children())==0:
		score=state.evaluate()
		return score
	
	if maximize:
		score=-10**10
		
		"""for etat in states:
			score=max(score,minimax_alphabeta(etat,T/len(states), False))
			if beta<=score:
				return score
			alpha=max(alpha,score)"""
		for i in range(len(states)):
			t2=time()
			t3=t2-t1
			score=max(score,minimax_alphabeta(states[i],(T-t3)/(len(states)-i), False))
			t1=t2
			T=T-t3
			if beta<=score:
				return score
			alpha=max(alpha,score)
	else:
		score=10**10
		"""for etat in state.get_children():
			score=min(score,minimax_alphabeta(etat,T/len(states), True))  
			if alpha>=score:
				return score
			beta=min(beta,score)"""
			for i in range(len(states)):
			t2=time()
			t3=t2-t1
			score=min(score,minimax_alphabeta(states[i],(T-t3)/(len(states)-i), False))
			t1=t2
			T=T-t3
			if alpha>=score:
				return score
			beta=min(beta,score)
	return(score)
