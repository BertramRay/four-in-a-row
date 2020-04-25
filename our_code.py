## _____                  ___            _      ____
# |  ___|__  _   _ _ __  |_ _|_ __      / \    |  _ \ _____      __
# | |_ / _ \| | | | '__|  | || '_ \    / _ \   | |_) / _ \ \ /\ / /
# |  _| (_) | |_| | |     | || | | |  / ___ \  |  _ < (_) \ V  V /
# |_|  \___/ \__,_|_|    |___|_| |_| /_/   \_\ |_| \_\___/ \_/\_/
#

botName='testonly'#实际运行时请换上自己的botname

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
def isWin( gameState ):
    # 参数当前状态gameState
    # 返回bool类型，是否我们胜利（我们为在棋盘上为0）
    # 还可以改进比如剩余距离和当前连在一起数量小于4，可不查！
    column = False #代表竖着的是否有四个连着的0
    for i in range(7) :#i代表列
        j = 5 
        number_continuuum = 0 #连着0的数量
        while j >= 0 and number_continuuum < 4 : 
            if gameState["Board"][j][i]== 0 :
                number_continuuum += 1
                j -= 1 
            else : 
                number_continuuum = 0
                j -= 1 
        if number_continuuum == 4 : #只检查4个
            column = True
            break

    row = False #代表横着的是否有四个连着的0
    for j in range(5, 0, -1) :#j代表行
        i = 0
        number_continuuum = 0 #连着0的数量
        while i < 7 and number_continuuum < 4 : 
            if gameState["Board"][j][i] == 0 :
                number_continuuum += 1
                i += 1 
            else : 
                number_continuuum = 0
                i += 1 
        if number_continuuum == 4 : #只检查4个
            row = True
            break

    biasl = False #代表携着的是否有四个连着的0,端点在0列的
    for k in range(6) :#k代表可行的斜线
        l = 6 - min( 5 - k , k - 0 ) #代表第k个斜线的长度
        m = 0 
        number_continuuum = 0 #连着0的数量
        if  k < 3 :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k+m][m] == 0 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasl = True
                break
        else :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k-m][m] == 0 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasl = True
                break
    
    biasr = False #代表携着的是否有四个连着的0,端点在6列的
    for k in range(6) :#k代表可行的斜线
        l = 6 -  min( 5 - k , k - 0 ) #代表第k个斜线的长度
        m = 0 
        number_continuuum = 0 #连着0的数量
        if  k < 3 :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k+m][6-m] == 0 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasr = True
                break
        else :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k-m][6-m] == 0 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasr = True
                break
    
    win = column or row or biasl or biasr 
    return win


def isLose( gameState ):
    # 参数当前状态gameState
    # 返回bool类型，是否对方赢（对方在棋盘上为1）
    # 还可以改进比如剩余距离和当前连在一起数量小于4，可不查！
    column = False #代表竖着的是否有四个连着的1
    for i in range(7) :#i代表列
        j = 5 
        number_continuuum = 0 #连着0的数量
        while j >= 0 and number_continuuum < 4 : 
            if gameState["Board"][j][i] == 1 :
                number_continuuum += 1
                j -= 1 
            else : 
                number_continuuum = 0
                j -= 1 
        if number_continuuum == 4 : #只检查4个
            column = True
            break

    row = False #代表横着的是否有四个连着的0
    for j in range(5, 0, -1) :#j代表行
        i = 0
        number_continuuum = 0 #连着0的数量
        while i < 7 and number_continuuum < 4 : 
            if gameState["Board"][j][i] == 1 :
                number_continuuum += 1
                i += 1 
            else : 
                number_continuuum = 0
                i += 1 
        if number_continuuum == 4 : #只检查4个
            row = True
            break

    biasl = False #代表携着的是否有四个连着的1,端点在0列的
    for k in range(6) :#k代表可行的斜线
        l = 6 -  min( 5 - k , k - 0 ) #代表第k个斜线的长度
        m = 0 
        number_continuuum = 0 #连着0的数量
        if  k < 3 :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k+m][m] == 1 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasl = True
                break
        else :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k-m][m] == 1:
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasl = True
                break
    
    biasr = False #代表携着的是否有四个连着的0,端点在6列的
    for k in range(6) :#k代表可行的斜线
        l = 6 -  min( 5 - k , k - 0 ) #代表第k个斜线的长度
        m = 0 
        number_continuuum = 0 #连着0的数量
        if  k < 3 :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k+m][6-m] == 1 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasr = True
                break
        else :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k-m][6-m] == 1:
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasr = True
                break
    
    lose = column or row or biasl or biasr 
    return lose


def isDraw( gameState ):
    # 参数当前状态gameState
    # 返回bool类型，是否平局
    draw = True 
    # 检查是否有棋子未下
    for j in range(5, 0, -1) :
          for i in range(7) :
              if gameState["Board"][j][i]== -1:
                  draw = False
                  return draw
    
    win = isWin(gameState )
    lose = isLose(gameState )
    if ( win == True ) or ( lose == True ):
        draw = False
    
    return draw
    
#def islose(gameState):
    
    
def test(gameState):
    dropColumn=randint(0, len(gameState["Board"][0])-1)
    while isColumnFullX(dropColumn,gameState["Board"]):
        dropColumn=randint(0, len(gameState["Board"][0])-1)
    return dropColumn

def getLegalActions(gameState):
    # 返回一个List，List包含可下棋子的列的编号（注意从0开始！）
    # 注意缺少保护！针对特殊情况
    legalActions = []
    for i in range(7):
        if gameState["Board"][0][i] == -1 : #只检查最上面一行
            legalActions.append(i)

    return legalActions
    
import copy
def getSuccessor(gameState , action , color):
    # 参数action 代表新的棋子所在列的编号（注意从0开始！）
    # 参数color 代表新的棋子的颜色
    # 返回一个gameState 表示操作后的状态
    # 注意缺少保护！针对特殊情况
    # 检查是否非法
    if  gameState["Board"][0][action] != -1  :
        return Exception #不处理只抛出异常！可以继续修改

    state = copy.deepcopy(gameState) #Json 对象的深拷贝
    i = 5 #从最底层找新棋子的位置
    while i >= 0 : 
        if state["Board"][i][action] != -1  :
            i -= 1
            continue
        else :
            state["Board"][i][action] = color 
            break

    return  state     
    
def ExpectimaxAgent( gameState , limitDepth ):
    # 参数当前状态gameState
    # 返回期望最大的动作
    maxValue = -float('inf')
    maxAction = None
    for action in getLegalActions(gameState):
        # 注意getSuccessor是自己下棋后的状态，棋子颜色为0
        tempValue = getExpect( getSuccessor(gameState , action , 0 ), limitDepth , 0 ) 
        if tempValue > maxValue:
            maxValue = tempValue 
            maxAction = action
    return maxAction

def getMax(gameState, limitDepth , depth = 0):
    # 参数当前状态gameState
    # 返回最大的评估值
    legalActions = getLegalActions(gameState)
    # 如果游戏停止，返回当前状态评估值
    if isWin(gameState) or  isLose(gameState) or isDraw(gameState) or depth == limitDepth :
        return evaluationFunction(gameState)

    maxValue = -float('inf')
    for action in legalActions:
        # 注意getSuccessor是自己下棋后的状态，棋子颜色为0
        tempValue = getExpect(getSuccessor(gameState , action , 0 ), limitDepth , depth)
        if tempValue > maxValue:
            maxValue = tempValue
    return maxValue 

def getExpect(gameState, limitDepth , depth = 0):  
    # 参数当前状态gameState
    # 返回平均的评估值
    legalActions = getLegalActions(gameState)

    # 如果游戏停止，返回当前状态评估值
    if isWin(gameState) or  isLose(gameState) or isDraw(gameState) or depth == limitDepth :
        return evaluationFunction(gameState)

    n = len(legalActions)
    sumValue = 0

    for action in legalActions :
        # 注意getSuccessor是对方下棋后的状态，棋子颜色为1
        sumValue += getMax( getSuccessor(gameState , action , 1 ), limitDepth , depth+1)
    expectValue = float( sumValue / n )
    
    return expectValue
    
def evaluationFunction(gameState):
    if isWin(gameState):
        return 100
    if isLose(gameState):
        return -1000000
    return 1
    #gameState["Board"]
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
    return {"Column": minimaxAgent(gameState,2)}


