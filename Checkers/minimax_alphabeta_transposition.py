def minimax(state, max_depth,maximize, get_children, evaluate, alpha=-10**10, beta=10**10,dic={}):
# calculer le score ici à l’aide de state.get_children() et state.evaluate()
    
    if max_depth==0 or len(get_children(state))==0:
        score=evaluate(state)
        if hash(state) in dic:
            score=dic[state]
        else:
            score=evaluate(state)
            dic[state]=score
        return score

    if maximize:
        score=-10**10
        for etat in get_children(state):
            score=max(score,minimax(etat,max_depth-1, False, get_children, evaluate))
            if beta<=score:
                return score
            alpha=max(alpha,score)

    else:
        score=10**10
        for etat in get_children(state):
            score=min(score,minimax(etat,max_depth-1, True, get_children, evaluate))  
            if alpha>=score:
                return score
            beta=min(beta,score)
    return(score)



