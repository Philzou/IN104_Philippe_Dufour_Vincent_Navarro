def minimax_alphabeta(state, max_depth,maximize, alpha=-10**10, beta=10**10):
# calculer le score ici à l’aide de state.get_children() et state.evaluate()

	if max_depth==0 or len(state.get_children())==0:
		score=state.evaluate()
		return score

	if maximize:
		score=-10**10
		for etat in state.get_children():
			score=max(score,minimax_alphabeta(etat,max_depth-1, False))
			if beta<=score:
				return score
			alpha=max(alpha,score)

	else:
		score=10**10
		for etat in state.get_children():
			score=min(score,minimax_alphabeta(etat,max_depth-1, True))  
			if alpha>=score:
				return score
			beta=min(beta,score)
	return(score)
