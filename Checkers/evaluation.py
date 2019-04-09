import IN104_simulateur as simu 
def evaluate(gs):
	Cell = simu.Cell
	score = 0
	for cell in gs.boardState.cells:
		if cell is Cell.w: score += 1
		elif cell is Cell.b : score -= 1
	return score
