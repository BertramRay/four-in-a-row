
botName='1615000492-defbot'

import json
from random import randint




# These are the only additional libraries available to you. Uncomment them
# to use them in your solution.
#
#import numpy    # Base N-dimensional array package
#import pandas   # Data structures & analysis
def isColumnFullX(dropColumn,board):
    #Check the top row has an empty space
    if len([x[dropColumn] for x in board if x[dropColumn] == -1]) > 0:
        return False

    return True


#def iswin(gameState):

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
#def islose(gameState):
    
    
def test(gameState):
    dropColumn=randint(0, len(gameState["Board"][0])-1)
    while isColumnFullX(dropColumn,gameState["Board"]):
        dropColumn=randint(0, len(gameState["Board"][0])-1)
    return dropColumn

def getLegalAction(gameStateBoard):
    # 返回一个List，List包含可下棋子的列的编号（注意从0开始！）
    # 注意缺少保护！针对特殊情况
    legalActions = []
    for i in range(7):
        if gameStateBoard[0][i] == -1 : #只检查最上面一行
            legalActions.append(i)

    return legalActions
    
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
    
    
def ExpectimaxAgent( gameStateBoard , limitDepth ):
    # 参数当前状态gameState
    # 返回期望最大的动作
    maxValue = -float('inf')
    maxAction = None
    for action in getLegalAction(gameStateBoard):
        # 注意getSuccessor是自己下棋后的状态，棋子颜色为0
        ( tempStateBoard, tempx )=getSuccessor( gameStateBoard, action, 0 )
        tempValue = getExpect( tempStateBoard, tempx, action, limitDepth, 0 ) 
        if tempValue > maxValue:
            maxValue = tempValue 
            maxAction = action
    return maxAction

def getMax(gameStateBoard, x, y, limitDepth , depth = 0):
    # 参数当前状态gameState
    # 返回最大的评估值
    legalActions = getLegalAction(gameStateBoard)
    # 如果游戏停止，返回当前状态评估值
    if isWin(gameStateBoard, x, y, 1) or  isDraw(gameStateBoard, x, y, 1) or depth == limitDepth :
        return evaluationFunction(gameStateBoard, x, y, 1)

    maxValue = -float('inf')
    for action in legalActions:
        # 注意getSuccessor是自己下棋后的状态，棋子颜色为0
        ( tempStateBoard, tempx )= getSuccessor(gameStateBoard , action , 0 )
        tempValue = getExpect( tempStateBoard, tempx , action, limitDepth , depth)
        if tempValue > maxValue:
            maxValue = tempValue
    return maxValue 

def getExpect(gameStateBoard, x, y, limitDepth , depth = 0):  
    # 参数当前状态gameState
    # 返回平均的评估值
    legalActions = getLegalAction(gameStateBoard)

    # 如果游戏停止，返回当前状态评估值
    if isWin(gameStateBoard, x, y, 0) or isDraw(gameStateBoard, x, y, 0) or depth == limitDepth :
        return evaluationFunction(gameStateBoard, x, y, 0)

    n = len(legalActions)
    sumValue = 0

    for action in legalActions :
        # 注意getSuccessor是对方下棋后的状态，棋子颜色为1
        ( tempStateBoard, tempx )= getSuccessor(gameStateBoard , action , 1 )
        sumValue += getMax( tempStateBoard, tempx, action,limitDepth, depth+1)
    expectValue = float( sumValue / n )
    
    return expectValue
    
def evaluationFunction(gameStateBoard, x , y , color ):
    return evaluationFunction1(gameStateBoard)
    
def evaluationFunction1(board):
    #constant
    COLUMN = 7
    ROW = 6
    FOUR = 2000000
    ALIVE_3 =  100000
    DEAD_3 = 1000
    ALIVE_2 = 800
    DEAD_2 = 5
    ALIVE_1 = 3
    DEAD_1 = 1    
    
    #variables
    value = 0.0
    cal_board = board
    cal_top = [] #每列实际列顶，列空：cal_top[i] = ROW,列满:cal_top[i] = 0 
    #计算cal_top
    for j in range(COLUMN):
        for i in range(ROW):
            if cal_board[i][j] != -1:
                cal_top.append(i)
                break
            if i == ROW-1:
                cal_top.append(ROW)
    print(cal_top)

    #第一维：棋形。第二维：玩家和机器人
    d = [[0]*2 for i in range(5)]#d[5][2]
    a = [[0]*2 for i in range(4)]#a[4][2]
    #活眼加权值
    cons = [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125]
    
        
    #methods
    def cal(player):#type为0或1，表示计算的是玩家或机器人的各棋形数
        #横向
        for i in range(ROW):
            j = 0
            while ((j<COLUMN) and (cal_board[i][j] != player)):
                j += 1
            while (j<COLUMN):
                x = j
                while ((j<COLUMN) and (cal_board[i][j] == player)):
                    j += 1
                if ((j-x) >= 4):
                    d[4][player] += 1
                else:
                    if (((x == 0) and (cal_board[i][j] == -1)) or ((x != 0) and (j != COLUMN) and (cal_board[i][x-1] != -1) and (cal_board[i][j] == -1))):
                        d[j-x][player] += cons[cal_top[j]-i-1]
                    else:
                        if (((j == COLUMN) and (cal_board[i][x - 1] == -1)) or ((x != 0) and (j != COLUMN) and (cal_board[i][x - 1] == -1) and (cal_board[i][j] != -1))):
                            d[j - x][player] += cons[cal_top[x - 1] - i - 1]
                        else:
                            if ((x != 0) and (j != COLUMN) and (cal_board[i][x-1] == -1) and (cal_board[i][j] == -1)):
                                a[j - x][player] += cons[int((cal_top[x - 1] + cal_top[j]) / 2) - i - 1]
                while((j < COLUMN) and (cal_board[i][j] != player)):
                    j += 1
        #纵向
        for i in range(COLUMN):
            j = cal_top[i]
            if ((j != 0) and (j != ROW) and (cal_board[j][i] == player) and (cal_board[j - 1][i] == -1)):
                x = j
                while ((j < ROW) and (cal_board[j][i] == player)):
                    j += 1
                if ((j - x) >= 4):
                    d[4][player] += 1
                else:
                    d[j - x][player] += 1
        #左下-右上
        for i in range(1,ROW + COLUMN):
            # x: c_row y: c_column
            if (i < ROW):
                x = i
                y = 0
            else:
                x = ROW - 1
                y = i - x
            while ((x != -1) and (y != COLUMN) and (cal_board[x][y] != player)):
                x -= 1
                y += 1
            while (((x != -1) and (y != COLUMN))):
                j = 0
                xx = x
                yy = y
                while ((x != -1) and (y != COLUMN) and (cal_board[x][y] == player)):
                    x -= 1
                    y += 1
                    j += 1
                if (j >= 4):
                    d[4][player] += 1
                else:
                    if (((xx != ROW -1) and (yy != 0)) or ((x != -1) and (y != COLUMN))):#不与棋盘左下或右上边缘相接
                        if ((not((xx != ROW -1) and (yy != 0)) and (cal_board[x][y] == -1)) or ((xx != ROW -1) and (yy != 0) and (x != -1) and (y != COLUMN) and (cal_board[xx + 1][yy - 1] != -1) and (cal_board[x][y] == -1))):
                            d[j][player] += cons[cal_top[y] - x - 1]
                        else:
                            if ((not((x != -1) and (y != COLUMN)) and (cal_board[xx + 1][yy - 1] == -1)) or ((xx != ROW -1) and (yy != 0) and (x != -1) and (y != COLUMN) and (cal_board[xx + 1][yy - 1] == -1) and (cal_board[x][y] != -1))):
                                d[j][player] += cons[cal_top[yy - 1] - xx - 2]
                            else:
                                if((xx != ROW -1) and (yy != 0) and (x != -1) and (y != COLUMN) and (cal_board[xx + 1][yy - 1] == -1) and (cal_board[x][y] == -1)):
                                    a[j][player] += cons[int((cal_top[yy - 1] - xx + cal_top[y] - 3 - x) / 2)]
                while ((x != -1) and (y != COLUMN) and (cal_board[x][y] != player)):
                    x -= 1
                    y += 1
                                    
        #左上-右下
        for i in range(1, ROW + COLUMN -2):
            if (i < ROW):
                x = ROW - 1 - i
                y = 0
            else:
                x = 0
                y = i + 1 - ROW
            while ((x != ROW) and (y != COLUMN) and (cal_board[x][y] != player)):
                x += 1
                y += 1
            while (((x != ROW) and (y != COLUMN))):
                j = 0
                xx = x
                yy = y
                while ((x != ROW) and (y != COLUMN) and (cal_board[x][y] == player)):
                    x += 1
                    y += 1
                    j += 1
                if (j >= 4):
                    d[4][player] += 1
                else:
                    if ((xx * yy != 0) or ((x != ROW) and (y != COLUMN))):#不与棋盘右上或左下边缘相接
                        if ( (not(xx * yy != 0) and (cal_board[x][y] == -1)) or ((xx * yy != 0) and (x != ROW) and (y != COLUMN) and (cal_board[xx - 1][yy - 1] != -1) and (cal_board[x][y] == -1))):
                            d[j][player] += cons[cal_top[y] - x - 1]
                        else:
                            if((not((x != ROW) and (y != COLUMN)) and (cal_board[xx - 1][yy - 1] == -1)) or ((xx * yy != 0) and (x != ROW) and (y != COLUMN) and (cal_board[xx - 1][yy - 1] == -1) and (cal_board[x][y] != -1))):
                                d[j][player] += cons[cal_top[yy - 1] - xx]
                            else:
                                if((not((x != ROW) and (y != COLUMN)) and (cal_board[xx - 1][yy - 1] == -1)) or ((xx * yy != 0) and (x != ROW) and (y != COLUMN) and (cal_board[xx - 1][yy - 1] == -1) and (cal_board[x][y] != -1))):
                                    d[j][player] += cons[cal_top[yy - 1] - xx]
                                else:
                                    if ((xx * yy != 0) and (x != ROW) and (y != COLUMN) and (cal_board[xx - 1][yy - 1] == -1) and (cal_board[x][y] == -1)):
                                        a[j][player] += cons[int((cal_top[yy - 1] - xx + cal_top[y] - x - 1)/2)]
                while ((x != ROW) and (y != COLUMN) and (cal_board[x][y] != player)):
                    x += 1
                    y += 1
        return 0
    
    #main
    cal(0)
    value+=d[4][0]*FOUR+d[3][0]*DEAD_3+d[2][0]*DEAD_2+d[1][0]*DEAD_1+a[3][0]*ALIVE_3+a[2][0]*ALIVE_2+a[1][0]*ALIVE_1
    cal(1)
    value-=d[4][1]*FOUR+d[3][1]*DEAD_3+d[2][1]*DEAD_2+d[1][1]*DEAD_1+a[3][1]*ALIVE_3+a[2][1]*ALIVE_2+a[1][1]*ALIVE_1
    return value
    
    # board = [[-1, 0, 1, 1, -1, -1, -1], 
    #          [-1, 0, 0, 1, -1, -1, -1], 
    #          [-1, 0, 0, 0,  1, -1, -1], 
    #          [-1, 1, 1, 0,  1, -1, -1], 
    #          [-1, 0, 1, 1,  1, -1, -1], 
    #          [-1, 1, 1, 0,  0,  0,  0]]
    # i = evaluationFunction(board)
    # print(i)

#minimaxAgent
def minimaxAgent(gameState,limitDepth):
    def max_value(c_state,c_depth,alpha,beta):
        v=-float('inf')
        if c_depth>limitDepth:
            return evaluationFunction(c_state)
        actions=getLegalActions(c_state)
        if isWin(c_state) or  isLose(c_state) or isDraw(c_state):
            return evaluationFunction(c_state)
        for action in actions:
            v=max(min_value(getSuccessor(c_state,action,0),c_depth,alpha,beta),v)
            if v>beta:
                return v
            alpha=max(alpha,v)
        return v

    def min_value(c_state,c_depth,alpha,beta):
        v=float('inf')
        actions=getLegalActions(c_state)
        if isWin(c_state) or  isLose(c_state) or isDraw(c_state):
            return evaluationFunction(c_state)
        for action in actions:
            v=min(max_value(getSuccessor(c_state,action,1),c_depth+1,alpha,beta),v)
            if v<alpha:
                return v
            beta=min(beta,v)
        return v

    actions=getLegalActions(gameState)
    va=-float('inf')
    alpha=-float('inf')
    beta=float('inf')
    exp=[]
    for action in actions:
        li=min_value(getSuccessor(gameState,action,0),1,alpha,beta)
        exp.append(li)
        va=max(li,va)
        alpha=max(alpha,va)
    return actions[exp.index(max(exp))]

# =============================================================================
# This calculateMove() function is where you need to write your code. When it
# is first loaded, it will play a complete game for you using the Helper
# functions that are defined below. The Helper functions give great example
# code that shows you how to manipulate the data you receive and the move
# that you have to return.
#

def calculateMove(gameState):

    # When manipulating the Board remember the positions are as follows
    #
    # 0| -   -   -   -   -   -   -
    # 1| -   -   -   -   -   -   -
    # 2| -   -   -   -   -   -   -
    # 3| -   R   R   Y   Y   -   -
    # 4| -   Y   R   R   R   -   -
    # 5| Y   R   R   Y   Y   -   Y
    # ----------------------------
    #    0   1   2   3   4   5   6
    #
    #
    # 0|-1  -1  -1  -1  -1  -1  -1
    # 1|-1  -1  -1  -1  -1  -1  -1
    # 2|-1  -1  -1  -1  -1  -1  -1
    # 3|-1   1   1   0   0  -1  -1
    # 4|-1   0   1   1   1  -1  -1
    # 5| 0   1   1   0   0  -1   0
    # ----------------------------
    #    0   1   2   3   4   5   6
    #
    # -1 - Empty space
    #  0 - Your disc in this case yellow (Y)
    #  1 - Your opponents disc red (R)
    '''
    print(gameState)
    #makes a random drop in any column that is not full
    dropColumn=randint(0, len(gameState["Board"][0])-1)
    while isColumnFullX(dropColumn,gameState["Board"]):
        dropColumn=randint(0, len(gameState["Board"][0])-1)
    '''
    return {"Column":ExpectimaxAgent(gameState["Board"],2)}

def isColumnFullX(dropColumn,board):
    #Check the top row has an empty space
    if len([x[dropColumn] for x in board if x[dropColumn] == -1]) > 0:
        return False

    return True
