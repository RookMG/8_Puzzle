from search import Problem
from .state import State

class EightPuzzle(Problem) :
    def __init__(self, initial, goal):
        self.initial = initial
        self.previousVisited = set()
        print('initial state is...')
        print(initial)
        self.goal = goal

    def getActions(self) :
        return {
            "UP",
            "DOWN",
            "LEFT",
            "RIGHT"
        }

    def actions(self, state) :
        self.previousVisited.add(self.tupleState(state))
        return self.getValidAction(state, self.getActions())

    def result(self, state, action) :
        state = State(state, action)
        #print(state.state)
        #print(state.move())
        return state.move()

    def tupleState(self, state):
        return tuple(tuple(lists) for lists in state)

    def getValidAction(self, state, allActions) :
        valid = list()
        for act in allActions :
            check = State(state, act)
            if check.isActionValid :
                if self.tupleState(check.move()) in self.previousVisited:
                    pass
                else :
                    valid.append(act)
        #print("state, valid")
        #print(state)
        #print(valid)
        return valid
    
    def goal_test(self, state) :
        return state == self.goal
