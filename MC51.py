botName='testonly'

import json
from random import randint

import math
import copy

avalible_choices = [ 0, 0, 0, 0, 0, 0, 0] 
"""
0代表该选择是合法的但尚未创建该节点，1代表该选择是合法的且已经创建，-1代表该选择非法。其中list的序号对应列编号（0-6）。每次实验区初始化
"""
avalible_actions=[] #即avalible_choices中合法（不为-1）的index
top=[] #avalibe_actions中每列顶端（第一个没有棋子的位置）
existed_childs = []
"""
用于记录已经存在的node节点
"""
total_visit_times = 0
all_expanded=False

class Node(object):
    """
    用于七个选择节点的类。包含选择的列编号（0-6），累计的reward，被访问次数。
    """
    def __init__(self): 
        """
        参数为空，构造函数
        """   
        self.visit_times = 0 #被访问次数
        self.reward_value = 0.0 #累计的reward
        self.choice = 0 #选择的列编号（0-6）

    def get_visit_times(self):
        """
        参数为空，返回被访问的次数
        读节点被访问次数
        """
        return self.visit_times

    def get_reward_value(self):
        """
        参数为空，返回累计的reward
        读节点累计的reward
        """
        return self.reward_value
    
    def get_choice(self):
        """
        参数为空，返回选择的列编号
        读节点选择的列编号
        """
        return self.choice
 
    def set_visit_times(self, times):
        """
        参数为节点被访问次数，返回空
        写节点被访问次数
        """
        self.visit_times = times

    def set_reward_value(self, value):
        """
        参数为节点累计的reward，返回空
        写节点被访问次数
        """
        self.reward_value = value
    
    def set_choice(self, choice):
        """
        参数为选择的列编号，返回空
        写节点选择的列编号
        """
        self.choice = choice


def get_legal_action( board ):
    """
    参数为最开始的棋盘二维数组，返回空
    用于初始化Avalible_Choices
    """
    for i in range(7):
        if  board[0][i] == -1 :
            avalible_choices[i] = 0
            avalible_actions.append(i)#修改

        else:
            avalible_choices[i] = -1


def release():#修改

    """
    参数为空，返回空
    全部初始化
    """
    global all_expanded
    all_expanded = False
    global total_visit_times
    total_visit_times = 0 
    existed_childs.clear()
    avalible_actions.clear()
    top.clear()


def is_all_expanded():#修改，去循环
    """
    参数为空，返回布尔类型
    用于判断是否所有合法的节点都被创建
    属于tree_policy使用函数
    """
    global all_expanded
    if all_expanded:
       return True
    for i in range(7):
        if avalible_choices[i] == 0 :
            return False
    all_expanded = True
    return True
    # for i in range(7):
    #     if avalible_choices[i] == 0 :
    #         return False
    # return True
    # if existed_node_number==7:
    #     return True
    # else:
    #     return False

def next_unexpanded():#修改，去循环
    """
    参数为空，返回int代表选择的列编号
    用于找到尚未被创建的节点
    属于expand使用函数
    """
    #没有保护
    for i in range(7):
        if avalible_choices[i] == 0 :
            return i
    # return avalible_actions[0]


def tree_policy( ):
    """
    参数为空，返回node节点
    用于给出这次实验选择的节点
    """

    if is_all_expanded():
        node = best_child()
        return node
    else:
        node = expand()
        return node

def expand():
    """
    参数为空，返回node节点
    用于创建一个尚未被创建的节点
    属于tree_policy使用函数
    """
    action = next_unexpanded()
    avalible_choices[action]=1
    new_node = Node()
    new_node.set_choice(action)
    existed_childs.append(new_node)
    return new_node

def best_child():
    """
    参数为空，返回node节点
    用于选择UCB值最高的节点
    属于tree_policy使用函数
    """
    best_score = -float('inf')
    best_node = None
    C = 100 #/ math.sqrt(2.0)
    for node in existed_childs:
        left = node.get_reward_value() / node.get_visit_times()
        right = 2.0 * math.log( total_visit_times ) / node.get_visit_times()
        score = left + C*math.sqrt(right)

        if score > best_score :
            best_score = score
            best_node = node
    
    return best_node

def isWin( gameStateBoard, x , y , color):
    # 参数当前状态gameState
    # 参数当前状态x , y是action为新棋子的位置，color为新棋子颜色
    # 返回bool类型，是否当前颜色胜利
    # 还可以改进比如剩余距离和当前连在一起数量小于4，可不查！
    # 检查竖着的是否有四个以上连着
    number_continuuum = 1 #已经计入新的棋子
    t=x+1
    while t<=5 and gameStateBoard[t][y] == color:#t代表行
        t+=1
    number_continuuum += ( t-x-1 ) 
    if number_continuuum >= 4 :
        return True

    #检查横着的是否有四个以上连着
    number_continuuum = 1 #已经计入新的棋子
    t=y+1
    while t<7 and gameStateBoard[x][t]==color:
        t+=1
    # for j in range( y + 1, 7, 1) :#j代表行
    #     if gameStateBoard[x][j] != color:
    #         t = j 
    #         break
    number_continuuum += ( t - y-1 )
    t=y-1
    while t>-1 and gameStateBoard[x][t]==color:
        t-=1
    # for j in range( y - 1, -1, -1) :#j代表行
    #     if gameStateBoard[x][j] != color:
    #         t = j 
    #         break
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

def getSuccessor(gameStateBoard, action):
    # 参数action 代表新的棋子所在列的编号（注意从0开始！）
    # 参数color 代表新的棋子的颜色
    # 返回action对应的行信息
    # 注意缺少保护！针对特殊情况
    # 检查是否非法
    #print("GTS")
    if  gameStateBoard[0][action] != -1  :
        #print("Exception")
        return Exception #不处理只抛出异常！可以继续修改

    i = 5 #从最底层找新棋子的位置
    while i >= 0 : 
        if gameStateBoard[i][action] != -1  :
            i -= 1
        else:
            break

    return  i  
 
def default_policy( board, node):
    """
    参数为node节点，初始棋盘二维数组board，返回float类型的reward 。
    用于对给出的选择进行一次模拟
    本函数若平局则award=0，赢则award>0，步数越多得分越低，输则award<0，步数越多得分越高
    """
    #node.set_visit_times(node.get_visit_times()+1)#修改访问次数
    cur_action=copy.deepcopy(avalible_actions)#模拟棋局中的legal action list
    successor=copy.deepcopy(top)
    stateboard=copy.deepcopy(board)

    # cur_move=node.get_choice()#当前棋路
    # stateboard[successor[cur_move]][cur_move]=0#我方棋子下棋
    # successor[cur_move]-=1#修改棋盘每列的top
    # if successor[cur_move]<0: #判断并修改legal action
    #     cur_action.pop(cur_move)
    #     successor.pop(cur_move)
    # length=len(cur_action) #可选move的长度
    cur_move=node.get_choice()#当前棋路
    index=cur_action.index(cur_move)
    stateboard[successor[index]][cur_move]=0#我方棋子下棋
    
    if isWin(stateboard,successor[index],cur_action[index],0):
        del stateboard
        del cur_action
        del successor
        return 100000
    
    successor[index]-=1#修改棋盘每列的top
    if successor[index]<0: #判断并修改legal action
        cur_action.pop(index)
        successor.pop(index)
    length=len(cur_action) #可选move的长度

    # import random
    award=0
    color=1 #对手先下
    move=0 #下棋步数
    while length!=0:
        index=randint(0,length-1) #随机选取后继
        stateboard[successor[index]][cur_action[index]]=color
        if isWin(stateboard,successor[index],cur_action[index],color):
            if color==0:#我方赢
                award+=10000
                break
            if color==1:#对方赢
                award-=100000
                # print("输了输了")
                # print(move)
                # print(node.get_choice())
                break
        
        successor[index]-=1
        if successor[index]<0:
            successor.pop(index)
            cur_action.pop(index)
            length-=1
        color=1-color #换对手
        move+=1
    award*=0.1**move#我方赢步数越多得分越低，对方赢步数越多得分越高
    del stateboard
    del cur_action
    del successor
    return award

def backup(node, reward):
    """
    参数为node节点，模拟的reward（float），返回空
    用于更新node节点的visit_times、reward_value
    """
    node.visit_times+=1
    node.reward_value+=reward

def best_child_final():
    """
    参数为空，返回node节点
    用于选择UCB值最高的节点
    属于tree_policy使用函数
    """
    best_score = -float('inf')
    best_node = None
    C = 0
    for node in existed_childs:
        left = node.get_reward_value() / node.get_visit_times()
        right = 2.0 * math.log( total_visit_times ) / node.get_visit_times()
        score = left + C*math.sqrt(right)

        if score > best_score :
            best_score = score
            best_node = node
    
    return best_node

def final_choice():
    """
    输入为空，返回为int代表选择的列编号
    用于给出整个实验结束后的最佳选择
    """
    return best_child_final().get_choice()
    # existed_childs.sort(key=lambda a:a.visit_times,reverse=True)
    # # print("OK")
    # # print(existed_childs[0].get_visit_times())
    # # print(existed_childs[0].get_choice())
    # return existed_childs[0].get_choice()

def monte_carlo_tree_search(board):
    """
    输入为初始棋盘二维数组，返回为int代表选择的列编号
    用于函数的整合，顶层函数
    """
    #print("2")
    computation_budget = 10000
    #所有节点的总的访问次数清空
    global total_visit_times
    total_visit_times = 0 
    #找到所有的合法选择
    get_legal_action( board )
    #print("4")
    #print(avalible_actions)
    for action in avalible_actions:#添加
        #print("5")
        #print(getSuccessor(board,action))
        top.append(getSuccessor(board,action))
    #print("3")
    for i in range(computation_budget):
        #所有节点的总的访问次数+1
       #print("OK")
        total_visit_times += 1

        expand_node = tree_policy()
        #print("OK")
        reward = default_policy(board ,expand_node)

        backup(expand_node, reward)
        #print("OK")
        
#     for childs in existed_childs:
#         print(childs.visit_times)
#         print(childs.reward_value)
#         print(childs.reward_value/childs.visit_times)
#         print(childs.choice)

    # print(existed_childs[0].visit_times)
    # print(existed_childs[1].visit_times)
    # print(existed_childs[2].visit_times)
    # print(existed_childs[3].visit_times)
    # print(existed_childs[4].visit_times)
    # print(existed_childs[5].visit_times)
    # print(existed_childs[6].visit_times)
    # print(existed_childs[0].reward_value)
    # print(existed_childs[1].reward_value)
    # print(existed_childs[2].reward_value)
    # print(existed_childs[3].reward_value)
    # print(existed_childs[4].reward_value)
    # print(existed_childs[5].reward_value)
    # print(existed_childs[6].reward_value)
    # print(existed_childs[0].reward_value/existed_childs[0].visit_times)
    # print(existed_childs[1].reward_value/existed_childs[1].visit_times)
    # print(existed_childs[2].reward_value/existed_childs[2].visit_times)
    # print(existed_childs[3].reward_value/existed_childs[3].visit_times)
    # print(existed_childs[4].reward_value/existed_childs[4].visit_times)
    # print(existed_childs[5].reward_value/existed_childs[5].visit_times)
    # print(existed_childs[6].reward_value/existed_childs[6].visit_times)
    # print(existed_childs[0].choice)
    # print(existed_childs[1].choice)
    # print(existed_childs[2].choice)
    # print(existed_childs[3].choice)
    # print(existed_childs[4].choice)
    # print(existed_childs[5].choice)
    # print(existed_childs[6].choice)
    action=final_choice()
    # print(top)
    #清空existed_childs
    release()

    return action

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

    #print(gameState["Board"])

    #makes a random drop in any column that is not full
    # dropColumn=randint(0, len(gameState["Board"][0])-1)
    # while isColumnFullX(dropColumn,gameState["Board"]):
    #     dropColumn=randint(0, len(gameState["Board"][0])-1)
    #print("1")
    return {"Column": monte_carlo_tree_search(gameState["Board"])}

def isColumnFullX(dropColumn,board):
    #Check the top row has an empty space
    if len([x[dropColumn] for x in board if x[dropColumn] == -1]) > 0:
        return False

    return True
