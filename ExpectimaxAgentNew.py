def ExpectimaxAgent( gameState , limitDepth ):
    # 参数当前状态gameState
    # 返回期望最大的动作
    maxValue = -float('inf')
    maxAction = None
    for action in getLegalAction(gameState):
        # 注意getSuccessor是自己下棋后的状态，棋子颜色为0
        ( tempState, tempx )=getSuccessor( gameState, action, 0 )
        tempValue = getExpect( tempState, tempx, action, limitDepth, 0 ) 
        if tempValue > maxValue:
            maxValue = tempValue 
            maxAction = action
    return maxAction

def getMax(gameState, x, y, limitDepth , depth = 0):
    # 参数当前状态gameState
    # 返回最大的评估值
    legalActions = getLegalAction(gameState)
    # 如果游戏停止，返回当前状态评估值
    if isWin(gameState, x, y, 1) or  isDraw(gameState, x, y, 1) or depth == limitDepth :
        return evaluationFunction(gameState, x, y, 1)

    maxValue = -float('inf')
    for action in legalActions:
        # 注意getSuccessor是自己下棋后的状态，棋子颜色为0
        ( tempState, tempx )= getSuccessor(gameState , action , 0 )
        tempValue = getExpect( tempState, tempx , action, limitDepth , depth)
        if tempValue > maxValue:
            maxValue = tempValue
    return maxValue 

def getExpect(gameState, x, y, limitDepth , depth = 0):  
    # 参数当前状态gameState
    # 返回平均的评估值
    legalActions = getLegalAction(gameState)

    # 如果游戏停止，返回当前状态评估值
    if isWin(gameState, x, y, 0) or isDraw(gameState, x, y, 0) or depth == limitDepth :
        return evaluationFunction(gameState, x, y, 0)

    n = len(legalActions)
    sumValue = 0

    for action in legalActions :
        # 注意getSuccessor是对方下棋后的状态，棋子颜色为1
        ( tempState, tempx )= getSuccessor(gameState , action , 1 )
        sumValue += getMax( tempState, tempx, action,limitDepth, depth+1)
    expectValue = float( sumValue / n )
    
    return expectValue