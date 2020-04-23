#getLegalActions(gameState) return all the possible actions in a list
#evaluationFunction(gameState) return eva func
#getSuccessor(gameState , action , color) return nextgameState
#color=0 means our turn, color=1 means opponent's turn

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

'''
def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #This time we use another way to implement the algorithm
        def max_value(c_state,c_depth,alpha,beta):
            v=-999999
            if c_depth>self.depth:
                return self.evaluationFunction(c_state)
            actions=c_state.getLegalActions(0)
            if not actions:
                return self.evaluationFunction(c_state)
            for action in actions:
                li=min_value(c_state.generateSuccessor(0,action),1,c_depth,alpha,beta)
                v=max(li,v)
                if v>beta:
                    return v
                alpha=max(alpha,v)
            return v

        def min_value(c_state,c_agent_index,c_depth,alpha,beta):
            v=999999
            actions=c_state.getLegalActions(c_agent_index)
            if not actions:
                return self.evaluationFunction(c_state)
            for action in actions:
                if c_agent_index==gameState.getNumAgents()-1:
                    li=max_value(c_state.generateSuccessor(c_agent_index,action),c_depth+1,alpha,beta)
                else:
                    li=min_value(c_state.generateSuccessor(c_agent_index,action),c_agent_index+1,c_depth,alpha,beta)
                v=min(li,v)
                if v<alpha:
                    return v
                beta=min(beta,v)
            return v
        
        actions=gameState.getLegalActions(0)
        
        va=-999999
        alpha=-999999
        beta=999999
        exp=[]
        for action in actions:
            li=min_value(gameState.generateSuccessor(0,action),1,1,alpha,beta)
            exp.append(li)
            va=max(li,va)
            alpha=max(alpha,va)
        return actions[exp.index(max(exp))]
'''