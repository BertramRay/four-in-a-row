def evaluationFunction(gameState, x , y , color ):
    if color == 0:
        if isWin(gameState, x , y , color):
            return 100
    else:
        if isWin(gameState, x , y , color):
            return -1000000
    return 1