def evaluationFunction(board):
    
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
            if (j == 0):
                x = j
                while ((j < ROW) and (cal_board[j][i] == player)):
                    j += 1
                if ((j - x) >= 4):
                    d[4][player] += 1             
                continue
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
