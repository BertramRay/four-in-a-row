#getLegalAction(gameState) return all the possible actions in a list
#evaluationFunction(gameState) return eva func
#getSuccessor(gameStateBoard, action , color):
    # 参数action 代表新的棋子所在列的编号（注意从0开始！）
    # 参数color 代表新的棋子的颜色
    # 返回一个tuple (gameState,x ) 表示操作后的状态x , y为新棋子的位置，color为新棋子颜色
    # 注意缺少保护！针对特殊情况
    # 检查是否非法
#color=0 means our turn, color=1 means opponent's turn
#isWin( gameStateBoard, x , y , color):
    # 参数当前状态gameState
    # 参数当前状态x , y是action为新棋子的位置，color为新棋子颜色
    # 返回bool类型，是否当前颜色胜利
#isDraw( gameStateBoard , x , y , color ):
    # 参数当前状态gameState
    # 参数当前状态x , y为新棋子的位置，color为新棋子颜色
    # 返回bool类型，是否平局

def minimaxAgent(gameStateBoard,limitDepth):
    #c_state is a tuple: (currentBoard, height), height means the height of the most recent chess(also means x), currentBoard means the current state's board information.
    #horizon also means y, the horizontal coordinate of the most recent chess.
    def max_value(c_state,c_depth,alpha,beta,horizon):
        v=-float('inf')
        if c_depth>limitDepth:
            return evaluationFunction(c_state[0])
        actions=getLegalAction(c_state[0])
        if isWin(c_state[0],c_state[1],horizon,1) or isDraw(c_state[0],c_state[1],horizon,1):
            return evaluationFunction(c_state[0])
        for action in actions:
            v=max(min_value(getSuccessor(c_state[0],action,0),c_depth,alpha,beta,action),v)
            if v>beta:
                return v
            alpha=max(alpha,v)
        return v

    def min_value(c_state,c_depth,alpha,beta,horizon):
        v=float('inf')
        actions=getLegalAction(c_state[0])
        if isWin(c_state[0],c_state[1],horizon,0) or isDraw(c_state[0],c_state[1],horizon,0):
            return evaluationFunction(c_state[0])
        for action in actions:
            v=min(max_value(getSuccessor(c_state[0],action,1),c_depth+1,alpha,beta,action),v)
            if v<alpha:
                return v
            beta=min(beta,v)
        return v

    actions=getLegalAction(gameStateBoard)
    va=-float('inf')
    alpha=-float('inf')
    beta=float('inf')
    exp=[]
    for action in actions:
        li=min_value(getSuccessor(gameStateBoard,action,0),1,alpha,beta,action)
        exp.append(li)
        va=max(li,va)
        alpha=max(alpha,va)
    return actions[exp.index(max(exp))]