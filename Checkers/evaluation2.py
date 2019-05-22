import IN104_simulateur as simu 
def evaluate2(gs):
	Cell = simu.Cell
	score = 0
	for cell in gs.boardState.cells:
		if cell is Cell.w: score += 1
		elif cell is Cell.W: score +=3
		elif cell is Cell.b : score -= 1
		elif cell is Cell.B: score-=3
	
	return score
