
def minimax(state, max_depth, maximize):
# calculer le score ici à l’aide de state.get_children() et state.evaluate()

    if max_depth==0 or len(state.get_children())==0:
        score=state.evaluate()
        return score

    if maximize:
        score=-10**10
        for etat in state.get_children():
            score=max(score,minimax(etat,max_depth-1, False))
        return score

    else:
        score=10**10
        for etat in state.get_children():
            score=min(score,minimax(etat,max_depth-1, True))
        return score

