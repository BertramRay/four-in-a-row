def isWin( gameStateBoard, x , y , color):
    # 参数当前状态gameState
    # 参数当前状态x , y为新棋子的位置，color为新棋子颜色
    # 返回bool类型，是否当前颜色胜利
    # 还可以改进比如剩余距离和当前连在一起数量小于4，可不查！
    # 检查竖着的是否有四个以上连着
    number_continuuum = 1 #已经计入新的棋子
    t = 0
    for i in range( y + 1, 5, 1) :#i代表列
        if gameStateBoard[i][y] != color:
            t = i 
            break
    number_continuuum += ( t - x ) 
    if number_continuuum >= 4 :
        return True

    #检查横着的是否有四个以上连着
    number_continuuum = 1 #已经计入新的棋子
    for j in range( y + 1, 6, 1) :#j代表行
        if gameStateBoard[x][j] != color:
            t = j 
            break
    number_continuuum += ( t - y )
    for j in range( y - 1, 0, -1) :#j代表行
        if gameStateBoard[x][j] != color:
            t = j 
            break
    number_continuuum += ( y - 1 - t )        
    if number_continuuum >= 4 :
        return True

    #左上-右下
    number_continuuum = 1#已经计入新的棋子
    k = 1 
    while ( x - k ) >= 0 and ( y - k ) >= 0:
        if gameStateBoard[x - k][y - k] != color:
            break
        k += 1
    number_continuuum += k - 1 
    k = 1
    while ( x + k ) <= 5 and ( y + k ) <= 6:
        if gameStateBoard[x + k][y + k] != color:
            break
        k += 1
    number_continuuum += k - 1 
    if number_continuuum >= 4 :
        return  True

    #左下-右上
    number_continuuum = 1#已经计入新的棋子
    k = 1 
    while ( x - k ) >= 0 and ( y + k ) <= 6:
        if gameStateBoard[x - k][y + k] != color:
            break
        k += 1
    number_continuuum += k - 1 
    k = 1
    while ( x + k ) <= 5 and ( y - k ) >= 0:
        if gameStateBoard[x + k][y - k] != color:
            break
        k += 1
    number_continuuum += k - 1 
    if number_continuuum >= 4 :
        return True
    
    #不属于上述任何获胜的可能情况
    return False


def isDraw( gameStateBoard , x , y , color ):
    # 参数当前状态gameState
    # 参数当前状态x , y为新棋子的位置，color为新棋子颜色
    # 返回bool类型，是否平局
    # 检查是否有棋子未下
    for j in range(7) :
        if gameStateBoard[0][j]== -1:
            return False
    
    if isWin(gameStateBoard, x , y , color) == True  :
        return False

    #棋子已经下完，且无人胜利
    return True