def evaluationFunction(gameStateBoard, x , y , color ):
    if color == 0:
        if isWin(gameStateBoard, x , y , color):
            return 100
    else:
        if isWin(gameStateBoard, x , y , color):
            return -1000000
    return 1