from time import time

def minimax_alphabeta(state, T,maximize, alpha=-1000, beta=1000):
# calculer le score ici à l’aide de state.get_children() et state.evaluate()
	t1=time()
	temps=1e-4
	#print(' '*depth, T)
	if T<temps:
		score=state.evaluate()
		#print(' '*depth, 'eval')
		return score 
		
	states=state.get_children()
	N=len(states)
	if N==0:
		score=state.evaluate()
		return score 	
	if maximize:
		score=-10**10
		for i in range(N):
			t2=time()
			t3=t2-t1
			score=max(score,minimax_alphabeta(states[i], (T-t3)/(N-i), False ,alpha, beta, ))
			if beta<=score:
				return score
			alpha=max(alpha,score)
	else:
		score=10**10
		for i in range(N):
			t2=time()
			t3=t2-t1
			#print(T)
			score=min(score,minimax_alphabeta(states[i], (T-t3)/(N-i), True, alpha, beta, ))
			if alpha>=score:
				return score
			beta=min(beta,score)
	return(score)
