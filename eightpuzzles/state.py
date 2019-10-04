import operator
from copy import deepcopy


class State:

    def __init__(self, state, action):
        self.state = state
        self.action = action

    def searchBlankLocation(self):
        for i in range(0,3) :
            for j in range(0,3):
                if self.state[i][j] == 0:
                    return (i,j)

    def move(self):
        result = deepcopy(self.state)
        blank = self.searchBlankLocation()
        if self.action == "UP":
            result[blank[0]][blank[1]] = result[blank[0]-1][blank[1]]
            result[blank[0]-1][blank[1]] = 0
        if self.action == "DOWN":
            result[blank[0]][blank[1]] = result[blank[0]+1][blank[1]]
            result[blank[0]+1][blank[1]] = 0
        if self.action == "RIGHT":
            result[blank[0]][blank[1]] = result[blank[0]][blank[1]+1]
            result[blank[0]][blank[1]+1] = 0
        if self.action == "LEFT":
            result[blank[0]][blank[1]] = result[blank[0]][blank[1]-1]
            result[blank[0]][blank[1]-1] = 0
        #print(self.state)
        #print(self.action)
        #print(result)
        return result

    @property
    def isActionValid(self):
        self.valid = True
        blank = self.searchBlankLocation()
        if self.action == "UP":
            if blank[0] == 0:
                self.valid = False
        if self.action == "DOWN":
            if blank[0] == 2:
                self.valid = False
        if self.action == "LEFT":
            if blank[1] == 0:
                self.valid = False
        if self.action == "RIGHT":
            if blank[1] == 2:
                self.valid = False
        #print("***********")
        #print(self.action)
        #print(self.state)
        #print(self.valid)
        return self.valid
