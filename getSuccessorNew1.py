import copy
def getSuccessor(gameStateBoard, action , color):
    # 参数action 代表新的棋子所在列的编号（注意从0开始！）
    # 参数color 代表新的棋子的颜色
    # 返回一个tuple (gameState,x ) 表示操作后的状态x , y为新棋子的位置，color为新棋子颜色
    # 注意缺少保护！针对特殊情况
    # 检查是否非法
    if  gameStateBoard[0][action] != -1  :
        return Exception #不处理只抛出异常！可以继续修改

    stateBoard = copy.deepcopy(gameStateBoard) 
    i = 5 #从最底层找新棋子的位置
    while i >= 0 : 
        if stateBoard[i][action] != -1  :
            i -= 1
        else :
            stateBoard[i][action] = color 
            break

    return  (stateBoard , i   )   