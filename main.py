from eightpuzzles import EightPuzzle
from search import breadth_first_tree_search, depth_first_tree_search, Node
import time

def main() :
    problem = EightPuzzle([[7, 2, 4], [5, 0, 6], [8, 3, 1]], [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    #problem = EightPuzzle([[0, 2, 3], [1, 4, 5], [7, 8, 6]], [[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    startTime = time.time()
    result = breadth_first_tree_search(problem)
    #result = depth_first_tree_search(problem)
    endTime = time.time()
    print('걸린 시간 : ', endTime-startTime)
    printPathAndSolution(result)

def printPathAndSolution(result) :
    print('path is ...')
    print(Node.path(result))
    print('solution is ...')
    print(Node.solution(result))

if __name__ == "__main__" :
    main()
